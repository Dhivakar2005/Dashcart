from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

class LLMExplanationAgent:
    """
    Uses Flan-T5 to generate a concise explanation for why a product is a good match.
    """
    def __init__(self, model_name="google/flan-t5-small"):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            self.model.to(device)
            self.generator = pipeline(
                "text2text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                device=0 if torch.cuda.is_available() else -1
            )
        except Exception as e:
            print(f"Error initializing model: {e}")
            raise

    def generate_explanation(self, interests, product):
        if not interests or not isinstance(interests, list):
            return "Error: Interests must be a non-empty list."
        
        if not product or not isinstance(product, dict):
            return "Error: Product details must be a valid dictionary."
        
        product_name = product.get("product_name", "Unknown Product")
        category = product.get("category", "Unknown Category")

        clean_interests = ", ".join(interests)
        prompt = (
            f"User Interests: {clean_interests}. "
            f"Product: {product_name} (Category: {category}). "
            "In one concise sentence, explain why this product is a perfect match for the user. "
            "Answer only with the explanation."
        )

        try:
            response = self.generator(
                prompt,
                max_new_tokens=50,
                truncation=True,
                num_return_sequences=1,
                do_sample=True,
                temperature=0.4,
                top_p=0.85
            )
            generated_text = response[0]['generated_text'].strip()
            
            # Ensure only the explanation is returned
            sentences = [s.strip() for s in generated_text.split('.') if s.strip()]
            explanation = sentences[0] + '.' if sentences else generated_text
            return explanation
        except Exception as e:
            return f"Error generating explanation: {e}"
