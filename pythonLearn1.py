import pypff, pandas as pd, itertools, re 
from bs4 import BeautifulSoup as bs

# read a email export (.PST) file and parse information
# display the parsed information in a data frame
pst = pypff.file()
pst.open("EmailSample_small.pst")

def get_children(item):
    if 'older' in str(type(item)):
        return itertools.chain(*[get_children(item) for item in item.sub_items if item])
    elif 'essage' in str(type(item)):
        traveler_name = item.subject[25:item.subject.index(" Traveling to")]
        pnr_info = item.subject[item.subject.index("- ")+2:]
        header = item.get_transport_headers()
        index1 = header.index("Date: ")
        index2 = header.index("+", index1)
        received_time = pd.to_datetime(header[index1+6: index2])
        soup = bs(item.html_body, 'html.parser')
        travel_info_tabletext = soup.find('div', attrs={'class':'h2'}).parent.parent.parent.text
        travelinfo = travel_info_tabletext.split("Hotel Recommendations")
        
        city = travelinfo[0].replace("\n", "")
        dates = travelinfo[1].split(" – ")
        start = pd.to_datetime(dates[0])
        end = pd.to_datetime(dates[1])
        
        links_with_text = [a['href'] for a in soup.find_all('a', href=True) if "mailto:lkoppaka@gmail.com" in a['href']]
        
        hotelsinfo = [(x[x.index("reservation:%0D%0A%0D%0AHotel: ")+31:x.index("%0D%0ANights: ")], x[x.index("Rate/Night: ")+12 : x.index("%0D%0A%0D%0ACancellation")]) for x in links_with_text]
        
        return [(item.subject, item.html_body, item.identifier, received_time, traveler_name, pnr_info, city, start, end, hotelsinfo)] #, item.creation_time, item.delivery_time, item.html_body
    else:
        return None

messages = pd.DataFrame([message for message in get_children(pst.root_folder)], columns=['Subject', 'Body', 'Identifier', 'ReceivedTime', 'Name', 'Pnr', 'City', 'Start', 'End', 'Recommendations']).set_index('Identifier') #, 
pst.close()
messages
