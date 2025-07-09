# 🤖 Mô hình Trợ lý Trả lời Câu hỏi (Gradio + API)

Giao diện người dùng đơn giản sử dụng Gradio để gửi câu hỏi và lựa chọn đến mô hình AI qua API (ví dụ Flask hoặc FastAPI), và nhận lại đáp án phù hợp.

---

## 🧰 Yêu cầu hệ thống

- Python >= 3.8
- `venv` (môi trường ảo)
- Internet (nếu dùng ngrok hoặc gọi API ngoài)

---

## 🚀 Khởi động Server (Backend)

1. Mở và chạy file **`Server.ipynb`** trong Jupyter Notebook.
2. Khi chạy xong, bạn sẽ thấy đường dẫn `https://xxxxx.ngrok-free.app`.
3. Sao chép đường dẫn đó và cập nhật vào `API_URL` trong file **`app.py`** theo định dạng:
   ```python
   API_URL = "https://xxxxx.ngrok-free.app/chat"

## 🚀 Khởi động client
1. Tạo môi trường ảo
python -m venv venv

2.  Kích hoạt môi trường ảo
venv\Scripts\activate        # Windows
# hoặc
source venv/bin/activate     # macOS/Linux

3. Cài đặt thư viện
pip install -r requirements.txt

4. Chạy giao diện
python app.py


## Truy cập 
- http://localhost:7860