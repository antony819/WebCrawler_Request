# WebCrawler(Request) Tutorial
Actually the purpose of writing this is just for my self-learning. You guys feel free to read it.

# Things to do before start writing code

1. First, we ofc need to create a new file in your coding software. 

2. Type pip install requests in terminal. (this code means you want to download the request library here
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/7aaa4f93-e002-4277-90b7-de52878c328c)

3. Type import requests as req in your code (make sure you import the requests library in your code)
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/70b76fb8-6c02-4729-afdf-ecd53cf01dbe)

4. Type from openpxyl import Workbook (this code means from openpxyl module extract a class called Workbook for you to use. And the usage of this Workbook is helping you to create a excel file and you can put the output of your program into it.)
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/6af57c07-06ec-44fd-81b5-601e5ca8b312)

# Start
5. We define a variable called url. And here you can type the url of the website that you want to crawl.

* In here you should not just copy the link in the url bar.
* For example in here. lets take the example of https://hahow.in/courses?status=INCUBATING&page=1
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/3f8015e8-3b06-4372-a7e7-4a35607583a3)
 
* Video: https://youtu.be/ZYu-nI6RlmU
* In this video, first you need to highlight the one of those words that you want to crawl here and see if they are exist in the source code. If exists, then you can directly type the url into your code.
* If not you can click F12 button and right click and click the button in the bottom to access developer tool.
* Then you can click the network button and F5 to let the data that loaded from the website appeared in here. 
* You have to find the file like in the video which contain the data you want to crawl. (click "preview")
* 
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/42c640f0-2702-40ca-87bb-89542e78f274)

* After you found that this is the file you want. Then you can copy the url like in the video to your code.

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/2de6d790-7bbd-4be9-b64e-499a28467eb4)


6. Because we want to extract all the information in many pages. So i will set a for loop and let the program access all the page and crawl all the data.

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/a1e459da-fd99-4300-be1a-f7129c798a5f)

7. Then we also need to add the header here to avoid the issue that the access get blocked by the website.
![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/e4c6bc5b-c891-43f7-8b7c-925435ea49b6)

8. We have to type req.get(url, headers = header) to let the program access the machine and get code (then you will see the program output 200 and thats mean it access successsfully)

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/43cde9b8-44df-4685-b290-ecdf498b6f07)

9. Although the program gets the code, still it is not translated. So we have to type  root_json= r.json() to solve the problem.

![image](https://github.com/antony819/WebCrawler_Request/assets/107425290/a920c06e-687d-456f-abca-5ca35ca6a56c)

(Continue.....)
