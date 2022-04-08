from transformers import AutoModelForCausalLM

# Load pretrained model
model = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-neo-125M')

# Save model to the hub
model.save_pretrained('codelm-playground')
