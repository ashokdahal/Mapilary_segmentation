#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load Library
import urllib, json
import pandas as pd

#Load an Image Sequence provided by Mapillary in CSV format
list_image=pd.read_csv("Location of Image Sequence as CSV")

#Create an Empty List
is_building=list()

#Run through each and every Image and perform the segmentation (takes 10 Minutes for 500 Images)
for x in range(len(list_image)):
    print(x)
    key=list_image.iloc[x]['Key']
    url="https://a.mapillary.com/v3/object_detections/segmentations?client_id="your Client ID"k&image_keys="+key
    response = urllib.request.urlopen(url)
    data_temp = json.loads(response.read())
    length=len(data_temp['features'])
    has_building=False
    for x in range(length):
        temp=data_temp['features'][x]
        #Check if building has image or not
        if temp['properties']['value']=="construction--structure--building":
            has_building=True
            break
    is_building.append(has_building)
    
#Inform List that it has building or not
se = pd.Series(is_building)
list_image["is_building"]= se.values

#Save Updated Inofrmation
list_image.to_csv("Output with building true or false")

