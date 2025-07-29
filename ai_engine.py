from huggingface_hub import InferenceClient
from config import HF_API_KEY

class DeepSeekAI:
    def __init__(self):
        self.client = InferenceClient(
            provider="together",
            api_key=HF_API_KEY,
        )

    def analyze_shop_performance(self, shop_data):
        context = f"""
        Data Toko Tokopedia:
        - Nama: {shop_data['shop_name']}
        - Revenue: Rp {shop_data['revenue']:,}
        - Total Orders: {shop_data['orders']}
        - Conversion Rate: {shop_data['conversion_rate']}%
        - Rating Toko: {shop_data['rating']}
        Top Products:
        """
        for product in shop_data['products'][:3]:
            context += f"- {product['name']}: {product['sold']} terjual, rating {product['rating']}\n"
        prompt = context + """
        Sebagai AI expert e-commerce, berikan 4 insight singkat untuk optimasi toko ini.
        Format jawaban:
        1. [emoji] [insight]
        2. ...
        """
        response = self.client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        text = response.choices[0].message.content
        return [line for line in text.split("\n") if line.strip()][:4]

    def chat_response(self, question, shop_data):
        prompt = f"""
        Kamu adalah AI e-commerce Tokopedia. 
        Data toko:
        Revenue: Rp {shop_data['revenue']:,}
        Orders: {shop_data['orders']}
        Conversion: {shop_data['conversion_rate']}%
        Produk terlaris: {shop_data['products'][1]['name']} ({shop_data['products'][1]['sold']})
        Pertanyaan seller: {question}
        Jawab max 3-4 kalimat, actionable, dan spesifik!
        """
        completion = self.client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7,
        )
        return completion.choices[0].message.content
