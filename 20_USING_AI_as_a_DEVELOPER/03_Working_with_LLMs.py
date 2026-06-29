# ===========================================================================================================================================================
# HARDWARE NOTE: NVIDIA H100 vs. CONSUMER RTX SERIES
# ===========================================================================================================================================================
# While both are Nvidia GPUs, they are fundamentally different architectures:
 
# 1. Purpose: H100 is a headless data-center accelerator built entirely for enterprise AI training and LLMs.
#    RTX cards are client-side GPUs built for real-time 3D rendering, ray tracing, and gaming.
 
# 2. VRAM & Bandwidth: H100 uses up to 80GB of ultra-fast HBM3 memory to hold massive neural nets in memory.
#    RTX tops out at 24GB-32GB of GDDR6X, restricting it to smaller, localized batch sizes or quantized models.
 
# 3. Hardware Blocks: H100 packs heavy 4th-Gen Tensor Cores and a dedicated Transformer Engine to speed up matrix math.
#    RTX balances fewer Tensor Cores with dedicated RT (Ray Tracing) Cores and display pipelines.
 
# 4. Form Factor: H100 has no display outputs (HDMI/DP) and relies on server rack airflow. RTX is a standalone PCIe card with active fan cooling for standard PCs.
 
#     NOTE : TL;DR: H100 is an industrial data-crunching train; RTX is an agile graphics sports car.
# ==================================================================================================================================================================

# Even if we are sending prompt on our PC the prompt is being processed on OpenAI servers in case of ChatGPT.


key  ="API_Key"

from openai import OpenAI
client = OpenAI(api_key=key)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
        {
            "role": "user",
            "content": "complete this chat: Jack: Hey; Jill: How are you?; Jack: now what?; Jill:  ",
        }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


for choice in response.choices:
    print(choice.message.content)