
import fitz  

doc = fitz.open("Sksjdksnd3.pdf")
page_dict={}

page_no=1
for page_num in range(len(doc)):
    page_link_list=[]
    page = doc.load_page(page_num)
    links = page.get_links()
    for link in links:
        rect = link["from"]  ##(x0, y0, x1, y1)
        text = page.get_text("text", clip=rect)
        page_link_list.append({'des_page':int(link['page'])+1,'start_from':link['from'],'text':text})

    page_dict[page_no]=page_link_list
    print(page_dict)
    page_no+=1
    x=input()
    if x=='0':
        break

print(page_dict)


##    if links:
##        print(f"Page {page_num + 1}:")
##        for link in links:
##            print(link)









##import fitz  
##
##doc = fitz.open("AHMEDABAD METRO_CTC_Rev A_19.02.2025 (1).pdf")
##page_dict={}
##
##page_no=1
##page_link_list=[]
##page = doc.load_page(204)
##links = page.get_links()
##for link in links:
##    print(link)
##    rect = link["from"] ##(x0, y0, x1, y1)
##    text = page.get_text("text", clip=rect)
##    page_link_list.append({'des_page':int(link['page']),'start_from':link['from'],'des_points':link['viewrect'],'text':text})
##
##page_dict[page_no]=page_link_list
##print(page_dict)
##page_no+=1
##
##    
##print(page_dict)
