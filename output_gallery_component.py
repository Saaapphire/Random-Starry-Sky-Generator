import gradio as gr
import random

def process():
    starry_skys=[(random.choice([
        "https://cdn.pixabay.com/photo/2022/01/24/19/14/nebula-6964440_1280.jpg",
        "https://cdn.pixabay.com/photo/2022/11/25/19/20/rosette-nebula-7616742_1280.jpg",
        "https://cdn.pixabay.com/photo/2024/12/07/13/08/space-9250868_1280.jpg",
        "https://cdn.pixabay.com/photo/2016/11/29/05/45/astronomy-1867616_1280.jpg",
        "https://cdn.pixabay.com/photo/2016/11/21/12/30/milky-way-1845068_1280.jpg",
        "https://cdn.pixabay.com/photo/2017/08/08/00/33/constellations-2609647_1280.jpg",
        "https://cdn.pixabay.com/photo/2016/11/29/02/20/astronomy-1866822_1280.jpg",
        "https://cdn.pixabay.com/photo/2016/11/29/07/21/astronomy-1868065_1280.jpg",
        "https://cdn.pixabay.com/photo/2017/08/30/01/05/milky-way-2695569_1280.jpg",
        "https://cdn.pixabay.com/photo/2012/11/28/08/54/milky-way-67504_1280.jpg"

    ]),f"label {i}")
        for i in range(1,5)]
    return starry_skys

demo=gr.Interface(fn=process,inputs=None,outputs=gr.Gallery(),
                  title="Random Starry Sky Generator")
demo.launch(share=True)