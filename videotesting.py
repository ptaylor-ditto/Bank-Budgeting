import random, time, webbrowser
videos = ['https://www.youtube.com/watch?v=CVCuN_q1K_g', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=OQj4bQEu-xA', 'https://www.youtube.com/watch?v=vm112M4ToLM', 'https://www.youtube.com/watch?v=cvh0nX08nRw', 'https://www.youtube.com/watch?v=jDwVkXVHIqg', 'https://www.youtube.com/watch?v=wrdK57qgNqA', 'https://www.youtube.com/watch?v=gM4S9lPyUUA', 'https://www.youtube.com/watch?v=8zEQeHcKMXM', 'https://www.youtube.com/watch?v=NW-qSGZByH8']
videost = []
while True:
    webbrowser.open(random.choice(videos))
    time.sleep(5)