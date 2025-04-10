import os
from agents.customer_analysis_agent import CustomerAnalysisAgent
from agents.product_matching_agent import ProductMatchingAgent
from agents.llm_explanation_agent import LLMExplanationAgent
from agents.image_generation_agent import ImageGenerationAgent

DB_PATH = "smart_shopping.db"
IMAGE_FOLDER = "static/images"

def run_pipeline(customer_id):
    print("[DEBUG] run_pipeline called with customer_id=" + customer_id)

    # 1. Analyze Customer
    customer_agent = CustomerAnalysisAgent(DB_PATH)
    interests = customer_agent.analyze_customer(customer_id)
    print(f"[DEBUG] Customer {customer_id} Interests:", interests)

    # 2. Match Products
    product_agent = ProductMatchingAgent(DB_PATH)
    matched_products = product_agent.match_products(interests)
    print("[DEBUG] Matched Products:", matched_products)

    # 3. LLM Explanation
    explanation_agent = LLMExplanationAgent()
    image_agent = ImageGenerationAgent(output_folder=IMAGE_FOLDER)

    recommendations = []
    for idx, product in enumerate(matched_products, start=1):
        # Generate Explanation
        explanation = explanation_agent.generate_explanation(interests, product)

        # Generate image if not exists
        product_image = os.path.join(IMAGE_FOLDER, f"{product['product_id']}.png")
        if not os.path.exists(product_image):
            image_agent.generate_image(
                product_id=product["product_id"],
                product_name=product["product_name"],
                category=product["category"]
            )

        recommendations.append({
            "product": product,
            "explanation": explanation
        })

    print("[DEBUG] Finished run_pipeline, returning recommendations.")
    return recommendations

if __name__ == "__main__":
    # Testing pipeline for multiple IDs
    for cid in ["C1000", "C1020"]:
        print(f"\n[DEBUG] Testing customer_id: {cid}")
        recs = run_pipeline(cid)
        print(f"\n=== FINAL RECOMMENDATIONS for {cid} ===")
        if recs:
            for idx, rec in enumerate(recs, start=1):
                print(f"{idx}. Product: {rec['product']['product_name']}")
                print(f"   Explanation: {rec['explanation']}")
                print("-" * 40)
        else:
            print("No recommendations available.")
