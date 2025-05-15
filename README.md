# 🛒 DashCart : AI-Powered Shopping Recommendation System

This project is an intelligent shopping recommendation platform that delivers personalized product suggestions based on customer ID. It combines traditional data insights with advanced AI agents for a rich, dynamic recommendation experience.



## 💡 Key Features

- 🎯 Personalized recommendations per `customer_id`
- 🤖 AI-driven architecture with modular agents:
  - **Customer Analysis Agent** – Extracts customer insights from data
  - **Product Matching Agent** – Finds relevant products based on interests
  - **LLM Explanation Agent** – Generates human-like explanations for recommendations
  - **Image Generation Agent** – Creates dynamic product visuals
- 🗃️ SQLite-backed database (lightweight and portable)
- 🌐 Web interface built with Flask



## 🧠 Architecture Overview

    
    User Input (customer_id)
            |
            v
    Customer Analysis Agent
            |
            v
    Product Matching Agent
            |
            +--> For each product:
            |       - LLM Explanation Agent
            |       - Image Generation Agent
            |
            v
    Final Output: HTML page with product, explanation, image





## 📁 Project Structure

    ├── app.py
    ├── run_flow.py 
    ├── setup_db.py
    ├── smart_shopping.db 
    ├── agents/ 
    │ ├── customer_analysis_agent.py
    │ ├── product_matching_agent.py
    │ ├── llm_explanation_agent.py
    │ └── image_generation_agent.py
    ├── templates/
    │ ├── index.html
    | ├── base.html
    │ └── recommendations.html
    ├── static/css/js/images/ # Generated product images
    └── requirements.txt



## 🌐 Web App Demo
The Flask app (app.py) provides a UI to enter a customer_id and view recommendations with:

- Product name and category

- Personalized explanation

- AI-generated product image



## 📂 Dataset Overview
### 🧍‍♂ Customer Data Collection Columns
- Customer_ID
- Age
- Gender
- Location
- Browsing_History
- Purchase_History
- Customer_Segment
- Avg_Order_Value
- Holiday
- Season

### 📦 Product Recommendation Data Columns
- Product_ID
- Category
- Subcategory
- Price
- Brand
- Average_Rating_of_Similar_Products
- Product_Rating
- Customer_Review_Sentiment_Score
- Holiday
- Season
- Geographical_Location
- Similar_Product_List
- Probability_of_Recommendation

## 🚀 Getting Started

### 1. Clone the Repository

    
    git clone https://github.com/Dhivakar2005/Dashcart.git
    cd Dashcart

### 2. Create and Activate Virtual Environment
    
    python -m venv venv
    source venv/bin/activate

### 3. Install Dependencies
    
    pip install -r requirements.txt

### 4.Run Files(One-by-One)
    - setup_db.py
    - run_flow.py
    - app.py

## 🫱🏻‍🫲🏻 Contributions
We welcome contributions to the DashCart AI-Powered Shopping Recommendation System! Whether you’re fixing a bug, adding features, or improving documentation, your input helps make this project better.

## 📄 License
This project is licensed under the MIT License.

