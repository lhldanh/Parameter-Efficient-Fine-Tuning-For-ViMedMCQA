import gradio as gr
import requests
import datetime

API_URL = "https://913240ee2ab2.ngrok-free.app/chat"

def get_timestamp():
    return datetime.datetime.now().strftime("%H:%M")

def call_model_api(question, choices_str):
    if not question.strip() or not choices_str.strip():
        return "Vui lòng nhập đầy đủ câu hỏi và các lựa chọn."
    
    question = ''.join(c for c in question if c.isalnum() or c.isspace())

    try:
        choices = [c.strip() for c in choices_str.split(",") if c.strip()]
        payload = {"question": question, "choices": choices}
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction", "Không có kết quả.")
        else:
            prediction = f"Lỗi server: {response.status_code}"

        formatted_choices = "\n> ".join([f"{chr(65+i)}. {c}" for i, c in enumerate(choices)])
        final_output = (
            f"### Câu hỏi:\n> {question}\n\n"
            f"### Lựa chọn:\n> {formatted_choices}\n\n"
            f"### Dự đoán:\n> **{prediction}**"
        )
        return final_output

    except Exception as e:
        return f"Lỗi: {e}"

js_func = """
function refresh() {
    const url = new URL(window.location);

    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

custom_head = """
<!-- HTML Meta Tags -->
<title>Medical Question Answering Assistant</title>
<link rel="icon" href="https://cdn-icons-png.flaticon.com/512/4712/4712100.png" type="image/png">
<meta name="description" content="An open-source web application showcasing various features and capabilities.">

<!-- Facebook Meta Tags -->
<meta property="og:url" content="https://example.com">
<meta property="og:type" content="website">
<meta property="og:title" content="Sample App">
<meta property="og:description" content="An open-source web application showcasing various features and capabilities.">
<meta property="og:image" content="https://cdn.britannica.com/98/152298-050-8E45510A/Cheetah.jpg">

<!-- Twitter Meta Tags -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:creator" content="@example_user">
<meta name="twitter:title" content="Sample App">
<meta name="twitter:description" content="An open-source web application showcasing various features and capabilities.">
<meta name="twitter:image" content="https://cdn.britannica.com/98/152298-050-8E45510A/Cheetah.jpg">
<meta property="twitter:domain" content="example.com">
<meta property="twitter:url" content="https://example.com">  
"""


with gr.Blocks(
    js=js_func, 
    title="Medical Question Answering Assistant",   
    head= custom_head ,
    css="""
    body, .gradio-container {
        background-color: #212121;
        color: #ececf1 !important;
        font-family: 'Segoe UI', sans-serif;
    }

    #main-container {
        max-width: 1250px;
        margin: 50px auto;
        padding: 10px 20px;
        border-radius: 16px;
        background-color: #212121;
        width: 100%;
        color: #ececf1;
    }
    
    #title {
        font-weight: 500;
        color: #ffffff;
    }

    #desc {
        font-size: 1rem;
        color: #a0a0a0;
        text-align: center;
        margin-bottom: 24px;
        margin-top: 24px;
    }

    #logo {
        margin: 0 auto;
        background-color: #10a37f !important;
        border-radius: 20px;
    }
    
    #chatbot {
        border: none !important;
        outline: none !important;   
        height: auto !important;
        min-height: 150px !important;
        background-color: #212121 !important;
    }
    
    #chatbot .message {
        background-color: #212121 !important;
        border: none !important;
        outline: none !important;
    }
    
    #chatbot label {
        display: none !important;
    }
    
    .gr-chatbot {
        background-color: #212121 !important;
        color: #ffffff;
        border-radius: 12px;
        padding: 16px;
        font-size: 1rem;
    }

    textarea, input {
        background-color: #303030 !important;
        color: white !important;
        border: 1px solid #5e5f6b !important;
        border-radius: 20px !important;
        padding: 12px !important;
        font-size: 1rem !important;
    }

    label span {
        font-size: 1rem !important;
        font-weight: 600 !important;
    }

    label {
        color: #10a37f !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 4px !important;
    }
    
    .placeholder-content {
        background-color: #212121 !important;
        border: none;
        outline: none;
    }
    
    .bubble-wrap {
        background-color: #212121 !important;
        border: none !important;
        outline: none !important;
    }

    .row button {
        background-color: #10a37f !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 12px 24px !important;
        margin-top: 8px;
        transition: all 0.2s ease-in-out;
    }

    button:hover {
        background-color: #0e8a6a !important;
        transform: scale(1.02);
        box-shadow: 0 0 8px rgba(16,163,127,0.6);
    }
    
    .form {
        background-color: #27272a !important;
        border: none !important;
        outline: none !important;
        border-radius: 20px !important;
        padding: 8px !important;
    }
    
    #chatbot .message.user {
        background-color: #303030 !important;
    }
    
    #chatbot .message.user p {
        background-color: #303030 !important;   
        color: #ececf1 !important;
        padding: 12px !important;
        margin: 0 !important;
    }
    """

) as demo:

    with gr.Column(elem_id="main-container"):
        gr.HTML("""
    <div class="gradio-header" style="
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #303030;
        margin: 0 0 30px 0 !important;
        padding: 10px 20px !important;
        position: fixed;
        width: 100%;
        top: 0;
        left: 0;
        background-color: #212121;
        z-index: 1000 !important;
        "
        >
        <header id="title">
            AI Giải Đáp Câu Hỏi Y Tế
        </header>
        <details style="
            background-color: #212121;
            color: white;
            padding: 10px;
            border-radius: 8px;
            border: none;
            font-size: 0.95rem;
            width: fit-content;
            text-align: left;
            z-index: 1000;
            box-shadow: 0 0 12px rgba(16,163,127,0.4);
        ">
        <summary style="font-weight: 600; 
                        cursor: pointer;
                        color: white;
                        font-size: 1rem;
                        background-color: #10a37f;
                        border-radius: 8px;
                        padding: 4px 8px;
                        text-align: right;"
                        transition: all 0.3s ease;
                        >
            📘 README
        </summary>
        <div style="margin-top: 12px;">
            <h3 style="color: #10a37f;">❓ Cách sử dụng ứng dụng</h3>
            <ul style="list-style-type: upper-roman;">
                <li>📌 Nhập <strong>câu hỏi y khoa</strong> bạn muốn hỏi vào ô đầu tiên.</li>
                <li>📋 Nhập <strong>các phương án lựa chọn</strong>, cách nhau bằng dấu phẩy (,).</li>
                <li>🤖 Nhấn <strong>Gửi</strong> để hệ thống AI đưa ra phân tích và dự đoán đáp án.</li>
            </ul>
            <p style="color: #10a37f; font-size: 0.85rem;">Ví dụ: "Triệu chứng của cảm cúm là gì?" – "Ho và sốt, Đau chân, Mất trí nhớ, Đau tim"</p>
        </div>
        </details>
    </div>
    """)
        gr.Image(
            value="https://cdn-icons-png.flaticon.com/512/4712/4712100.png",
            width=96, height=96,
            show_label=False,
            container=False,
            elem_id="logo"
        )

        gr.Markdown("## Nhập câu hỏi và các lựa chọn. Mô hình AI sẽ giúp bạn phân tích và đưa ra đáp án phù hợp.", elem_id="desc")

        chatbot = gr.Chatbot(type="messages", elem_id="chatbot")

        question_input = gr.Textbox(
            label="Câu hỏi",
            placeholder="Ví dụ: Triệu chứng của cảm cúm là gì?",
            lines=2
        )
        choices_input = gr.Textbox(
            label="Các lựa chọn (phân cách bằng dấu phẩy ' , ')",
            placeholder="Ho và sốt, Đau chân, Mất trí nhớ, Đau tim",
            lines=2
        )

        with gr.Row():
            submit_btn = gr.Button("Gửi", variant="primary")
            clear_btn = gr.Button("Xoá")

    def on_submit(q, c, history):
        timestamp = get_timestamp()
        history.append({"role": "user", "content": f"<span style='font-size: 0.8em; font-weight: 400; color: gray;'>[{timestamp}]</span>\n **Question**: {q}\n **Choices**: {c}"})
        history.append({"role": "assistant", "content": "⏳ Đang phân tích..."})
        yield "", "", history

        reply = call_model_api(q, c)
        history[-1] = {"role": "assistant", "content": f"<span style='font-size: 0.8em; font-weight: 400; color: gray;'>[{get_timestamp()}]</span>\n {reply}"}
        yield "", "", history

    def on_clear():
        return "", "", []

    submit_btn.click(on_submit, inputs=[question_input, choices_input, chatbot], outputs=[question_input, choices_input, chatbot])
    clear_btn.click(on_clear, outputs=[question_input, choices_input, chatbot])

demo.launch()
