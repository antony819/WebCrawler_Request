import requests as req
from openpyxl import Workbook

wb = Workbook() #create a excel file
ws = wb.active #activate the excel file

title = ['courseName','author','price','preorder','numofsold'] #the information name(can type wt u want)
ws.append(title) #add the title

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
for i in range(28):
    url = 'https://api.hahow.in/api/liveEvents?limit=24&page='
    url = url + str(i)
    print(url)
    r = req.get(url, headers= header)
    print(r)

    root_json= r.json() 
    # "json" in python means dictionary translate the response data into python readable format

    for data in root_json['data']:
    #'data' means the file "liveEvents?limit=24&page=0" contain the dictionary "data" and that contain the data we want here
        course = []
        course.append(data['title']) #actually this means we just find the category we want from the dictionary
        creators = data['creators']
        if creators:
            creator_names = ', '.join(creator['name'] for creator in creators)
            course.append(creator_names)
        else:
            course.append('N/A') #if the category we want is a sub-category, then we need to type both the parent and the child
        if 'price' in data:
            course.append(data['price'])
        else:
            course.append('N/A')
        if 'preOrderedPrice' in data:#if preordered price category is exist then extract it
            course.append(data['preOrderedPrice'])
        else:
            course.append('N/A')
        if 'numSoldTickets' in data:#if numSoldTickets price category is exist then extract it
            course.append(data['numSoldTickets'])
        else:
            course.append('N/A')

        ws.append(course) #add the course array in excel file

wb.save('data.xlsx') #save the excel file
