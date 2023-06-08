# WebCrawler(Request) Tutorial
Actually, the purpose of writing this is just for my self-learning. You guys feel free to read it.

# Things to do before start writing code

1. First, we ofc need to create a new file in your coding software. 

2. Type pip install requests in the terminal. (this code means you want to download the request library here
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/7aaa4f93-e002-4277-90b7-de52878c328c)

3. Type import requests as req in your code (make sure you import the requests library in your code)
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/70b76fb8-6c02-4729-afdf-ecd53cf01dbe)

4. Type from openpxyl import Workbook (this code means from openpxyl module extracts a class called Workbook for you to use. And the usage of this Workbook helps you to create an Excel file, and you can put the output of your program into it.)
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/6af57c07-06ec-44fd-81b5-601e5ca8b312)

# Start
5. We define a variable called URL. And here, you can type the URL of the website that you want to crawl.

* In here, you should not just copy the link in the URL bar.
* For example here. let's take the example of https://hahow.in/courses?status=INCUBATING&page=1
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/3f8015e8-3b06-4372-a7e7-4a35607583a3)
 
* Video: https://youtu.be/ZYu-nI6RlmU
* In this video, first, you need to highlight one of those words that you want to crawl here and see if they exist in the source code. If it exists, then you can directly type the URL into your code.
* If not, you can click the F12 button and right-click and click the button at the bottom to access the developer tool.
* Then you can click the network button and F5 to let the data that loaded from the website appear here. 
* You have to find the file, like in the video, which contains the data you want to crawl. (click "preview")
* 
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/42c640f0-2702-40ca-87bb-89542e78f274)

* After you find that this is the file you want. Then you can copy the URL like in the video to your code.

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/2de6d790-7bbd-4be9-b64e-499a28467eb4)


6. Because we want to extract all the information in many pages. So I will set a for loop and let the program access all the pages and crawl all the data.

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/a1e459da-fd99-4300-be1a-f7129c798a5f)

7. Then we also need to add the header here to avoid the issue that the access gets blocked by the website.
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/e4c6bc5b-c891-43f7-8b7c-925435ea49b6)

8. We have to type req.get(URL, headers = header) to let the program access the machine and get code (then you will see the program output 200, and thats mean it accessed successfully)

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/43cde9b8-44df-4685-b290-ecdf498b6f07)

9. Although the program gets the code, it is still not translated. So we have to type  root_json= r.json() to solve the problem.

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/a920c06e-687d-456f-abca-5ca35ca6a56c)

10. And NOW, you finally can select the data you want to crawl.

# Crawl Data

1. First, ofc you need to create an array to store the data you want.

2. We need to set a for loop into the root_json
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/7f1ba164-5c2c-4efd-b9d4-9da4c254355b)
* the reason why I type data here is to select the directory called data. Coz the data we want to crawl is under here.
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/770bbbe7-6e23-4d92-9d4f-2eb41fdf0135)

3.Then, you can type the code course.append(data ['the name of the class you want to crawl'])
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/e6fcad43-cb53-4beb-a4cc-f166289a5e94)

* maybe you may have some questions about "the name of the class you want to crawl."
* in here means the class that stores the data that is being crawled.

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/52803989-d401-4a3f-ab62-050a7b758a2f)

* In here, let's take an example. I want the data "讓學英文成為日常：王梓沅大人的自學法則" and "1016". Then I have to change 
course.append(data ['the name of the class you want to crawl']) to course.append(data ['title']). And also course.append(data ['subscribedCount']). It is because "讓學英文成為日常：王梓沅大人的自學法則" belongs to the title class and "1016" belongs to subscriber count. So if I want to crawl those data, then I have to type the code above in order to let the program grab those data from the class I want.

# Extract the crawled data

1. First, we have to type wb = Workbook() to create a workbook called wb.
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/cfe37ebe-15db-40c9-8dba-eb91fd93a1b1)

2. Then type ws = wb.active to activate the workbook file
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/9aab19ea-1947-4cb7-9dee-1dced9856f97)

3. You can type the title you want like. if I want to collect the course name, author name, price, preorder number, and a number of sold, then I will create an array called title and input all of them in it and append.
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/c4734594-65db-44c4-910d-96f9e83f1491)


5. After you finished crawling the data, then you can type ws.append(course) to add the course array in the Excel file
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/ba6f6fd8-8c25-4436-90ee-9f07346eb83d)

6. At last type wb.save('data.xlsx') to save the excel file

7. Done!!!!

# Q&A session

Q: Why sometimes I face KeyError in the class that I want to crawl?

A: It is because not all of the data you want contain the same class. So you may have to add an if case that if there is a word called 'the class that contains error' in the data, then course.append. If not, then append 'N/A'

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/cca262c5-1113-4aab-9e7a-dae6cc09d158)

Q: Why I can't find the file that contains the data I want in finding url part?

A: It is because the web owner or designer don't want the user to crawl their data so easily. For the web owner, web crawler is their enemies. If in that case, you may use another web crawler called beautiful soup. I will teach you how to use it in the future.

Q: If I master this web crawler tool, Will I find a girlfriend?

A: No. Get to sleep, and you can find a perfect girlfriend in your dream.


Credit:
1. https://www.youtube.com/watch?v=xua4Gno7xLo&t=1876s a tutorial from GrandmaCan
2. me
