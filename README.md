# Parameter-Efficient-Fine-Tuning-For-ViMedMCQA

# 🤖 Mô hình Trợ lý Trả lời Câu hỏi (Fine-tune + API + Gradio UI)

Một hệ thống hoàn chỉnh gồm:
- ✅ Fine-tune mô hình ngôn ngữ lớn (LLM) bằng kỹ thuật LoRA với Unsloth
- ✅ Giao tiếp qua API (Flask/FastAPI)
- ✅ Giao diện người dùng với Gradio để gửi câu hỏi và nhận đáp án

---

## 📁 Cấu trúc dự án

```
📦project/
 ┣ 📜finetuning.ipynb                      # Fine-tune mô hình LLM với LoRA + RSLORA
 ┣ 📜evaluation_form.ipynb                 # Evaluation mô hình
 ┣ 📁deployment/                          # Thư mục triển khai API và giao diện
 ┃ ┣ 📜Server.ipynb                       # API backend (Flask hoặc FastAPI + ngrok)
 ┃ ┣ 📜app.py                             # Giao diện người dùng Gradio
 ┣ 📜requirements.txt                     # Các thư viện cần thiết
 ┣ 📜README.md                            # Tài liệu hướng dẫn
```

---

## 🧠 Fine-Tune Mô Hình Ngôn Ngữ (LLM)

Notebook `finetuning.ipynb` sử dụng thư viện **Unsloth** để fine-tune mô hình **LLaMA-3.2-1B 4bit** trên dataset **MedMCQA**, với kỹ thuật **LoRA + RSLORA** nhằm giảm chi phí huấn luyện nhưng vẫn giữ hiệu quả.

### ⚙️ Cấu hình chính:
- `r=16`, `lora_alpha=16`, `lora_dropout=0`
- `use_rslora=True` (ổn định gradient)
- Áp dụng vào các lớp: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `up_proj`, `down_proj`, `gate_proj`

> ✅ Mô hình sau khi huấn luyện được đẩy lên Hugging Face Hub hoặc lưu local để sử dụng inference qua API.

---

## 🚀 Khởi động Server (Backend API)

1. Mở và chạy file **`Server.ipynb`** trong Jupyter Notebook.
2. Khi chạy xong, một đường dẫn dạng `https://xxxxx.ngrok-free.app` sẽ xuất hiện.
3. Sao chép đường dẫn và cập nhật vào file `app.py`:
   ```python
   API_URL = "https://xxxxx.ngrok-free.app/chat"
   ```

---

## 🖥️ Giao Diện Người Dùng (Client Gradio)

### 1. Tạo môi trường ảo
```bash
python -m venv venv
```

### 2. Kích hoạt môi trường ảo
```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 4. Chạy ứng dụng Gradio
```bash
python app.py
```

- Truy cập tại: [http://localhost:7860](http://localhost:7860)

---

## 📚 Dataset & Mô Hình

- **Dataset**: [MedMCQA](https://huggingface.co/datasets/openlifescienceai/medmcqa)
- **Base model**: [`unsloth/Llama-3.2-1B-bnb-4bit`](https://huggingface.co/unsloth/Llama-3.2-1B-bnb-4bit)
- **Fine-tuning**: PEFT with LoRA + RSLoRA

---

## 🧠 Inference Demo

Ví dụ câu hỏi:

```
Question: What is the capital of France?
Choices:
A. Berlin
B. Paris
C. Madrid
D. Rome
Answer:
```

Mô hình sẽ trả lời: **B. Paris**

---

## 📎 Ghi chú

- Yêu cầu Python >= 3.8
- Nên chạy trên GPU (>= 12GB nếu fine-tune)
- Cần Internet nếu sử dụng ngrok cho API

---

## 📚 Tài liệu tham khảo

- [LoRA Paper (Hu et al., 2021)](https://arxiv.org/abs/2106.09685)
- [Unsloth GitHub](https://github.com/unslothai/unsloth)
- [MedMCQA Dataset](https://huggingface.co/datasets/openlifescienceai/medmcqa)

---

🛠️ **Tác giả**: [Tên bạn ở đây]  
📅 **Cập nhật lần cuối**: Tháng 7/2025
