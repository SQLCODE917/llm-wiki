# Local Models

```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B build && cmake --build build --config Release -j
```

Error:
```
Mac:llama.cpp DSerbarinov$ cmake -B build && cmake --build build --config Release -j
-bash: cmake: command not found
```

```
pip3 install --user cmake
export PATH="$HOME/Library/Python/$(python3 -c 'import sys;print(f"{sys.version_info.major}.{sys.version_info.minor}")')/bin:$PATH"
cmake --version
```

add to ~/.bash_profile:
```
export PATH="$HOME/Library/Python/$(python3 -c 'import sys;print(f"{sys.version_info.major}.{sys.version_info.minor}")')/bin:$PATH"
```

Do a "Hello world" test:

```
./build/bin/llama-cli -hf ggml-org/Qwen2.5-0.5B-Instruct-GGUF -p "Say hello in five words" -n 32
```

Error:
```
HTTPS is not supported. Please rebuild with one of:
  -DLLAMA_BUILD_BORINGSSL=ON
  -DLLAMA_BUILD_LIBRESSL=ON
  -DLLAMA_OPENSSL=ON (default, requires OpenSSL dev files installed)
```

```
cmake -B build -DLLAMA_BUILD_BORINGSSL=ON
cmake --build build --config Release -j
```

For 24 GB and a wiki/knowledge-base use case, here's the practical picture. macOS caps how much unified memory Metal will hand to the GPU at roughly 70–75%, so your real working budget is about 17–18 GB for model + context cache. That rules out the 20 GB Qwen 3.6-35B MoE file and makes the 16.8 GB 27B dense quant uncomfortably tight. The sweet spot for you is a 14B-class dense model, which leaves generous headroom for long context — and for a wiki use case, long context matters more than raw speed.
My recommendation: Qwen3-14B from the official Qwen GGUF repo — first-party, Apache 2.0, no third-party quantizer in the loop, which fits your no-workarounds preference. Qwen publishes it at Qwen/Qwen3-14B-GGUF and documents running it directly via llama.cpp's -hf flag: 

```
./build/bin/llama-cli -hf Qwen/Qwen3-14B-GGUF:Q4_K_M --jinja -c 16384 -p "What caused the Bronze Age collapse?"
```

While it's downloading, installing claude code:

```
curl -fsSL https://claude.ai/install.sh | bash
```

Verify:
```
claude --version
```

If the binary exists but isn't found, add ~/.local/bin to your PATH — in your case (bash), add this to ~/.bash_profile:

```
export PATH="$HOME/.local/bin:$PATH"
```

Set claude default model (claude-fable-5 jsut came out, evaluating:)

~/llm-wiki/.claude/settings.json
```
{
  "model": "claude-fable-5"
}
```
