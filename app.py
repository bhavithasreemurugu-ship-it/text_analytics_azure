from openai import AzureOpenAI

endpoint = "https://project25115-resource.services.ai.azure.com/"
api_key = "YOUR_AZURE_API_KEY"
deployment_name = "gpt-5-mini"

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-12-01-preview"
)

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "Indian capital"}
    ]
)

print(response.choices[0].message.content)
