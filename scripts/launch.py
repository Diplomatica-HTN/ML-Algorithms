from summarize import generate_summary
import bs4 as bs
import urllib.request
import re


def main():
    # data = """In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched to empower the next generation of students with AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, "With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. This will require more collaborations and training and working with AI. That’s why it has become more critical than ever for educational institutions to integrate new cloud and AI technologies. The program is an attempt to ramp up the institutional set-up and build capabilities among the educators to educate the workforce of tomorrow." The program aims to build up the cognitive skills and in-depth understanding of developing intelligent cloud connected solutions for applications across industry. Earlier in April this year, the company announced Microsoft Professional Program In AI as a learning track open to the public. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI and data science with a series of online courses which featured hands-on labs and expert instructors as well. This program also included developer-focused AI school that provided a bunch of assets to help build AI skills."""
    # sentences = 2

    # output = generate_summary(data, sentences) # data to be summarized based on the number of sentences
    # print('**Summary**\n\n', output, '\n')
    # print(type(output))

    scraped_data = urllib.request.urlopen('https://toronto.ctvnews.ca/ontario-health-minister-says-premier-has-been-around-after-last-public-appearance-three-weeks-ago-1.5590025')
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article,'lxml')

    paragraphs = parsed_article.find_all('p')
    article_text = ''
    for p in paragraphs:
        article_text += p.text
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    # print('**ORIGINAL** ', article_text, '**ORIGINAL**')
    text = 'Having a significant amount of experience in Machine Learning and Data Science through internships, building projects, and winning competitions, I have been inspired to continue my journey in artificial intelligence. The Inspirit AI Scholars program will allow me to explore my passion for tech, meet link-minded individuals, learn from industry experts, and solve real-world problems! I truly believe that my background in Python is a perfect fit for the program as I will be able to share my knowledge with others and continue educating myself on AI. Furthermore, this program will give me a platform to focus my efforts on building a meaningful AI project and solving a global issue. I am certain that my interests, experiences, and drive for social good perfectly align with the values at Inspirit AI. I am eager to see what lies ahead and I cannot wait for our journey to begin!'
    final_summary =  generate_summary(text, 5)

    print('-'*100, '\n', final_summary)

if __name__ == '__main__':
    main()