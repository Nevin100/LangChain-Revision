# 📖 Folder 3: Local Models

## 🎯 Objective

Download and run open-source LLMs locally without API keys. Leverage HuggingFace models for cost-free inference.

## 📚 Theory & Concepts

### **Local Models vs Cloud APIs**

| Aspect | Cloud API | Local Model |
|--------|-----------|-------------|
| Speed | Very Fast (LPU) | Slow (CPU/GPU) |
| Cost | Per-token billing | Free |
| Privacy | Cloud stored | Local only |
| Setup | Instant | Complex |
| Customization | Limited | Full control |
| Offline | ❌ | ✅ |

### **HuggingFace Ecosystem**

```
HuggingFace (Model Hub)
    ├── Pre-trained Models (billions)
    ├── Open-source Weights
    ├── Community Contributions
    └── Model Cards (documentation)

Popular Open Models:
├── Llama 2/3 (Meta) - Production grade
├── Mistral (Mistral AI) - Efficient
├── Falcon (TII) - Multilingual
├── GPT-2 (OpenAI) - Educational
└── DistilGPT-2 - Lightweight
```

### **Model Sizes & Trade-offs**

```
Model Size    | Speed   | Quality | VRAM Needed | Best For
─────────────────────────────────────────────────────────
7B (Small)    | ⚡⚡⚡  | ⭐⭐    | 8 GB        | Quick testing
13B (Medium)  | ⚡⚡   | ⭐⭐⭐  | 16 GB       | Production
70B (Large)   | ⚡    | ⭐⭐⭐⭐ | 64+ GB      | Complex tasks
```

### **DistilGPT-2 in This Folder**

```
DistilGPT-2
├── Size: 82M parameters (40% compressed from GPT-2)
├── Speed: Very fast (CPU acceptable)
├── Quality: Adequate for simple text generation
├── VRAM: <2 GB
└── Use: Education, lightweight inference
```

### **Inference Pipeline Concept**

```
Tokenization: "Hello world" → [7592, 25, 1186]
         ↓
Model Processing: Input tokens through transformer layers
         ↓
Token Generation: Next token prediction iteratively
         ↓
Sampling: Temperature-based selection
         ↓
Detokenization: [7592, 25, 1186] → "Hello world was great"
```

### **Temperature-Based Sampling**

```
Temperature = 0.0:
"The sky is blue" → Always same output (greedy)

Temperature = 1.0:
"The sky is [red/blue/green/purple/...weighted]"

Temperature = 2.0:
"The sky is [completely random tokens]"
```

## 📁 Files Overview

### **hugging_face.py**

```
Purpose: Local HuggingFace model loading aur inference
Key Component: HuggingFacePipeline
Main Model: distilgpt2
```

## 🔑 Key Learning Points

### **1. Model Download & Caching**

```python
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

# First run: Downloads model (~350MB for distilgpt2)
# Cached at: ~/.cache/huggingface/hub/

model = HuggingFacePipeline.from_model_id(
    model_id="distilgpt2",          # Model name from HuggingFace
    task="text-generation",         # Task type
    model_kwargs={"temperature": 0.7},
    pipeline_kwargs={"max_new_tokens": 100}
)
```

### **2. Key Parameters**

```python
# Model Kwargs
model_kwargs = {
    "temperature": 0.7,        # Randomness control
    "top_p": 0.9,             # Nucleus sampling
    "top_k": 50,              # Top-k sampling
}

# Pipeline Kwargs
pipeline_kwargs = {
    "max_new_tokens": 100,    # Output length limit
    "min_length": 10,         # Minimum output length
    "do_sample": True,        # Enable sampling
}
```

### **3. Inference Methods**

```python
# Single inference
response = model.invoke("Complete this: Python is")

# Streaming (real-time output)
for chunk in model.stream("Your prompt"):
    print(chunk, end="")

# Batch processing
prompts = ["Prompt 1", "Prompt 2"]
results = model.batch(prompts)
```

### **4. Device Selection (CPU vs GPU)**

```python
# Automatically uses GPU if available
# Force CPU:
import torch
device = "cpu"  # or "cuda" for GPU

model_kwargs = {
    "device": 0 if device == "cuda" else -1,  # 0 = GPU, -1 = CPU
}
```

## 💡 Practical Patterns

### **Pattern 1: Simple Text Generation**

```python
llm = HuggingFacePipeline.from_model_id(
    model_id="distilgpt2",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 50}
)

prompt = "Artificial Intelligence is"
result = llm.invoke(prompt)
print(result)
```

### **Pattern 2: Controlled Generation**

```python
model_kwargs = {
    "temperature": 0.0,        # Deterministic
    "top_p": 0.9,             # Diversity control
}

# Same prompt = same output
result1 = llm.invoke("Python is")
result2 = llm.invoke("Python is")  # Identical
```

### **Pattern 3: Different Models**

```python
# Change model easily
models = [
    "distilgpt2",              # Small
    "gpt2",                    # Medium
    "gpt2-large",              # Larger (need GPU)
]

for model_id in models:
    llm = HuggingFacePipeline.from_model_id(
        model_id=model_id,
        task="text-generation"
    )
    # Use llm
```

## 🔄 Comparison: Different HuggingFace Models

```
Model          | Size | Speed | Quality | GPU Need
──────────────────────────────────────────────────
distilgpt2     | 82M  | ⚡⚡⚡ | ⭐⭐    | No
gpt2           | 124M | ⚡⚡  | ⭐⭐⭐  | No
gpt2-large     | 355M | ⚡   | ⭐⭐⭐⭐ | Recommended
distilbert     | 67M  | ⚡⚡⚡ | N/A    | Classification
```

## 📊 Performance Metrics

### **DistilGPT-2 Benchmarks**

```
Device      | Inference Time | VRAM Usage | Throughput
─────────────────────────────────────────────────────
CPU         | 2-5 sec/token  | ~1 GB      | 0.2 tokens/sec
GPU (V100)  | 50ms/token     | 0.5 GB     | 20 tokens/sec
GPU (RTX)   | 100ms/token    | 0.3 GB     | 10 tokens/sec
```

## 🛠️ Installation & Setup

### **GPU Support (Optional)**

```bash
# For CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Or for ROCm (AMD)
pip install torch --index-url https://download.pytorch.org/whl/rocm5.7
```

### **CPU Only**

```bash
# Default PyTorch (CPU version)
pip install torch  # Already in requirements.txt
```

## 🎓 Advanced Concepts

### **Quantization (Model Compression)**

```
Original Model (VRAM)  → Quantized Model (VRAM)
FP32: 355M params → 1.4 GB    INT8: ~350 MB
```

### **Model Loading Strategies**

```python
# Strategy 1: Load entire model
model = HuggingFacePipeline.from_model_id(...)

# Strategy 2: Load with specific dtype
import torch
model_kwargs = {
    "torch_dtype": torch.float16  # Half precision
}

# Strategy 3: Load only on GPU when needed
model_kwargs = {
    "device": 0 if torch.cuda.is_available() else -1
}
```

## 📝 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| OOM (Out of Memory) | Use smaller model or GPU |
| Slow inference | Use smaller model or GPU |
| Poor quality | Use larger model or fine-tune |
| Download fails | Check internet, clear cache |

## 💡 Pro Tips

1. **Production**: Use quantized models (faster + memory efficient)
2. **Development**: Start with DistilGPT-2, upgrade later
3. **Batch Processing**: Process multiple prompts together for efficiency
4. **Caching**: First run slow hoga (download), 2nd run fast

## 🔗 Model Selection Guide

### **Choose Based on Your Needs**

```
Lightweight (CPU):
└── DistilGPT-2 / DistilBERT

Medium (GPU):
└── Llama 2 7B / Mistral 7B

Heavy (GPU with 24GB+):
└── Llama 2 13B / Llama 2 70B
```

## 📚 Related Topics

- **Folder 1**: API-based models (comparison)
- **Folder 2**: Chat with local models
- **Folder 4**: Embeddings with local models
- **Folder 5**: Structured outputs from local inference

## 🚀 Next Steps

1. Try different models aur compare results
2. Add error handling aur timeout management
3. Implement batch processing for efficiency
4. Explore fine-tuning for specific tasks

---

**Happy Local Inference! 🏠**