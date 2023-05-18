from pydantic import BaseModel

from labapp.model import NeuralNetworkCategory, NeuralNetwork, News


class NavigationItem(BaseModel):
    name: str
    url: str


nav_menu: list[NavigationItem] = [
    NavigationItem(name='Нейросети', url='/'),
    NavigationItem(name='Промты', url='#'),
    NavigationItem(name='Статьи', url='/news'),
    NavigationItem(name='Обучение', url='#'),
    NavigationItem(name='Контакты', url='/contacts')
]

undefined_category = NeuralNetworkCategory(name="Без категории")
chat_bot_category = NeuralNetworkCategory(name="Чат-бот")
illustration_category = NeuralNetworkCategory(name="Иллюстрация")
design_category = NeuralNetworkCategory(name="Дизайн")
audio_to_text_category = NeuralNetworkCategory(name="Аудио в текст")

neural_networks_categories = [
    undefined_category,
    chat_bot_category,
    illustration_category,
    design_category,
    audio_to_text_category,
]

neural_networks = [
    NeuralNetwork(name="ChatGPT", category=chat_bot_category, tasks="ответы на вопросы", field="учеба, программирование",
                  url="https://openai.com.ru/", img="img/t2t.png",
                  short_desc="чат-бот с искусственным интеллектом, разработанный компанией OpenAI и способный "
                             "работать в диалоговом режиме, поддерживающий запросы на естественных языках...",
                  desc="чат-бот с искусственным интеллектом, разработанный компанией OpenAI и способный работать в "
                       "диалоговом режиме, поддерживающий запросы на естественных языках. ChatGPT — большая языковая "
                       "модель, для тренировки которой использовались методы обучения с учителем и обучения с "
                       "подкреплением. Данный чат-бот основывается на другой языковой модели от OpenAI — GPT-3.5 — "
                       "улучшенной версии модели GPT-3. 14 марта 2023 года была выпущена языковая модель GPT-4, "
                       "доступная тестировщикам и платным подписчикам ChatGPT Plus. В новой версии у ИИ появилась "
                       "возможность обработки не только текста, но и картинок."),
    NeuralNetwork(name="Midjourney", category=illustration_category, tasks="текст в изображение", field="дизайн",
                  url="https://www.midjourney.com/", img="img/t2i.png",
                  short_desc="исследовательская компания и разрабатываемое её одноименное программное обеспечение "
                             "искусственного интеллекта, создающее изображения по текстовым описаниям...",
                  desc="исследовательская компания и разрабатываемое ею одноименное программное обеспечение "
                       "искусственного интеллекта, создающее изображения по текстовым описаниям. Наряду с "
                       "конкурентами на рынке генерации изображений для персонализированных медиа — приложениями "
                       "DALL-E от OpenAI и Stable Diffusion — использует технологии генеративно-состязательных "
                       "сетей..."),
    NeuralNetwork(name="Recraft", category=design_category, tasks="", field="",
                  url="https://www.midjourney.com/", img="img/t2i.png",
                  short_desc="бесплатный браузерный ИИ-генератор иллюстраций и убиратор фона. Recraft — бесконечный "
                       "холст, на котором в слоях можно генерировать векторную графику, иллюстрации и 3D-картинки...",
                  desc="бесплатный браузерный ИИ-генератор иллюстраций и убиратор фона. Recraft — бесконечный "
                       "холст, на котором в слоях можно генерировать векторную графику, иллюстрации и 3D-картинки..."),
    NeuralNetwork(name="Dropchat", category=chat_bot_category, tasks="", field="",
                  url="https://www.midjourney.com/", img="img/t2t.png",
                  short_desc="ChatGPT для пользовательских файлов, книг, PDF, веб-сайтов, URL-адресов YouTube, "
                       "позволяющей студентам общаться в чате...",
                  desc="ChatGPT для пользовательских файлов, книг, PDF, веб-сайтов, URL-адресов YouTube, "
                       "позволяющей студентам общаться в чате..."),
    NeuralNetwork(name="Vizcom", category=design_category, tasks="", field="",
                  url="https://www.midjourney.com/", img="img/t2i.png",
                  short_desc="создание 3D объекта из наброска, и его редактирование с помощью подсказок. Vizcom AI — "
                       "созданы, чтобы помочь...",
                  desc="создание 3D объекта из наброска, и его редактирование с помощью подсказок. Vizcom AI — "
                       "созданы, чтобы помочь..."),
    NeuralNetwork(name="Sonix", category=audio_to_text_category, tasks="", field="",
                  url="https://www.midjourney.com/", img="img/a2t.png",
                  short_desc="это мощное и простое в использовании онлайн-программное обеспечение для транскрипции "
                             "аудио, которое предлагает несколько функций, облегчающих процесс расшифровка "
                             "аудиофайлов проще и...",
                  desc="это мощное и простое в использовании онлайн-программное обеспечение для транскрипции аудио, "
                       "которое предлагает несколько функций, облегчающих процесс расшифровка аудиофайлов проще и..."),
]

news = [
    News(name="OpenAI в настоящее время не обучает GPT-5...",
         img="img/GPT-5.png",
         text="Эксперты, призывающие сделать паузу в развитии ИИ, будут рады услышать, что OpenAI в настоящее время не "
              "обучает GPT-5. Генеральный директор OpenAI Сэм Альтман удаленно выступил на мероприятии Массачусетского "
              "технологического института и был опрошен на тему ИИ компьютерным ученым и подкастером Лексом "
              "Фридманом.	Альтман подтвердил, что OpenAI в настоящее время не разрабатывает пятую версию своей "
              "модели Generative Pre-trained Transformer и вместо этого фокусируется на расширении возможностей "
              "GPT-4, последней версии."),
    News(name="Сбербанк представляет GigаСhat: новую нейронную сеть для многоязычного общения и творческих задач...",
         img="img/GigaChat.png",
         text="Сбербанк представил свою новую нейросеть, названную GigаСhat. На первом этапе она будет доступна в "
              "режиме тестирования по приглашениям. С помощью этой нейросети можно задавать вопросы, поддерживать "
              "диалог, писать программный код, а также создавать тексты и картинки на основе описаний в рамках "
              "единого контекста. При этом GigаСhat поддерживает мультимодальное взаимодействие и способна более "
              "грамотно общаться с пользователями на русском языке."),
    News(name="Подборка ИИ сервисов для работы с видео...",
         img="img/AI.png",
         text="В этой статье мы рассмотрим несколько ИИ-сервисов, которые могут быть использованы для работы с видео. "
              "Они предлагают различные инструменты, начиная от автоматического хромакея и создания текста в "
              "голосовой форме, заканчивая созданием видео на основе заданного текста и генерированием видео по "
              "запросу. Рассмотрим каждый из них подробнее и рассмотрим примеры, как они могут быть использованы для "
              "создания профессионального и интересного видео.</p> <p>Kaiber – это сервис, который позволяет "
              "загружать музыку и создавать видеоклипы на основе заданной темы и стиля. С помощью ИИ-алгоритмов "
              "Kaiber создает интересные и качественные видео.</p> <p>ZebraCat AI – это сервис, который генерирует "
              "видео по заданным запросам. С помощью машинного обучения и глубоких нейронных сетей ZebraCat AI "
              "создает уникальные и оригинальные видео, которые могут быть использованы для различных целей, "
              "в том числе для рекламных кампаний и продвижения бренда.</p> <p>Elai – это платформа преобразования "
              "текста в видео. С помощью ИИ и текстового анализа Elai позволяет создавать видео на основе заданного "
              "текста и озвучивать его с помощью диктора."),
]