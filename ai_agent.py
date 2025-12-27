!pip install wikipedia
import wikipedia
import gradio as gr

def ai_agent(question):
    if question.strip() == "":
        return "Please enter a question."

    try:
        return wikipedia.summary(question, sentences=5)

    except wikipedia.exceptions.DisambiguationError:
        return "Your question is ambiguous. Please be more specific."

    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find an answer to that."

    except Exception:
        return "Something went wrong. Please try again."


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🤖 Smart AI Agent
        *An intelligent AI agent that answers any question using AI and NLP*
        """
    )

    with gr.Row():
        question = gr.Textbox(
            label="Question",
            placeholder="Ask me any question...",
            lines=3
        )

    with gr.Row():
        output = gr.Textbox(
            label="Answer",
            lines=12,          # 🔥 BIG output box
            interactive=False
        )

    with gr.Row():
        submit = gr.Button("Submit", variant="primary")
        clear = gr.Button("Clear")

    submit.click(fn=ai_agent, inputs=question, outputs=output)
    clear.click(fn=lambda: ("", ""), inputs=None, outputs=[question, output])

demo.launch()
