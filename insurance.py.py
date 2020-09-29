#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import re


# In[ ]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

#China
country = 'China'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.cn.html'

all_data = []
for params['page'] in range(1, 2):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[78]:


# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

#Spain
country = 'Spain'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.es.html'

all_data = []
for params['page'] in range(1, 168):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[79]:


# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

#Italy
country = 'Italy'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.it.html'

all_data = []
for params['page'] in range(1, 72):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[80]:


# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

#UK
country = 'UK'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.gb.html'

all_data = []
for params['page'] in range(1, 66):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[81]:


# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

#Morocco
country = 'Morocco'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ma.html'

all_data = []
for params['page'] in range(1, 59):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[235]:


#United_States
country = 'United_States'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = United_States

all_data = []
for params['page'] in range(1, 53):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[236]:


#Colombia
country = 'Colombia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Colombia

all_data = []
for params['page'] in range(1, 48):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[237]:


#Israel
country = 'Israel'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Israel

all_data = []
for params['page'] in range(1, 25):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[238]:


#Switzerland
country = 'Switzerland'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Switzerland

all_data = []
for params['page'] in range(1, 12):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[239]:


#Finland
country = 'Finland'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Finland

all_data = []
for params['page'] in range(1, 12):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[240]:


#Russian_Federation
country = 'Russian_Federation'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Russian_Federation

all_data = []
for params['page'] in range(1, 10):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[241]:


#Uzbekistan
country = 'Uzbekistan'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Uzbekistan

all_data = []
for params['page'] in range(1, 9):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[242]:


#Austria
country = 'Austria'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Austria

all_data = []
for params['page'] in range(1, Austria_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[243]:


#Hong_Kong
country = 'Hong_Kong'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Hong_Kong

all_data = []
for params['page'] in range(1, Hong_Kong_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[244]:


#Denmark
country = 'Denmark'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Denmark

all_data = []
for params['page'] in range(1, Denmark_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[245]:


#Republic_Of_Korea
country = 'Republic_Of_Korea'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Republic_Of_Korea

all_data = []
for params['page'] in range(1, Republic_Of_Korea_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[246]:


#Australia
country = 'Australia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Australia

all_data = []
for params['page'] in range(1, Australia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[247]:


#Belgium
country = 'Belgium'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Belgium

all_data = []
for params['page'] in range(1, Belgium_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[248]:


#India
country = 'India'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = India

all_data = []
for params['page'] in range(1, India_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[249]:


#Ireland
country = 'Ireland'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Ireland

all_data = []
for params['page'] in range(1, Ireland_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[250]:


#Japan
country = 'Japan'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Japan

all_data = []
for params['page'] in range(1, Japan_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[251]:


#Singapore
country = 'Singapore'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Singapore

all_data = []
for params['page'] in range(1, Singapore_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[252]:


#Germany
country = 'Germany'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Germany

all_data = []
for params['page'] in range(1, Germany_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[253]:


#Vietnam
country = 'Vietnam'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Vietnam

all_data = []
for params['page'] in range(1, Vietnam_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[254]:


#Portugal
country = 'Portugal'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Portugal

all_data = []
for params['page'] in range(1, Portugal_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[255]:


#France
country = 'France'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = France

all_data = []
for params['page'] in range(1, France_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[256]:


#Greece
country = 'Greece'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Greece

all_data = []
for params['page'] in range(1, Greece_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[257]:


#South_Africa
country = 'South_Africa'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = South_Africa

all_data = []
for params['page'] in range(1, South_Africa_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[258]:


#Hungary
country = 'Hungary'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Hungary

all_data = []
for params['page'] in range(1, Hungary_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[259]:


#Chile
country = 'Chile'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Chile

all_data = []
for params['page'] in range(1, Chile_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[260]:


#Bulgaria
country = 'Bulgaria'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Bulgaria

all_data = []
for params['page'] in range(1, Bulgaria_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[261]:


#Canada
country = 'Canada'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Canada

all_data = []
for params['page'] in range(1, Canada_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[262]:


#Turkey
country = 'Turkey'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Turkey

all_data = []
for params['page'] in range(1, Turkey_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[263]:


#Romania
country = 'Romania'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Romania

all_data = []
for params['page'] in range(1, Romania_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[264]:


#Croatia
country = 'Croatia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Croatia

all_data = []
for params['page'] in range(1, Croatia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[265]:


#Estonia
country = 'Estonia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Estonia

all_data = []
for params['page'] in range(1, Estonia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[266]:


#Philippines
country = 'Philippines'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Philippines

all_data = []
for params['page'] in range(1, Philippines_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[267]:


#Serbia
country = 'Serbia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Serbia

all_data = []
for params['page'] in range(1, Serbia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[268]:


#Luxembourg
country = 'Luxembourg'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Luxembourg

all_data = []
for params['page'] in range(1, Luxembourg_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[269]:


#Bosnia_Herzegovina
country = 'Bosnia_Herzegovina'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Bosnia_Herzegovina

all_data = []
for params['page'] in range(1, Bosnia_Herzegovina_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[270]:


#Nigeria
country = 'Nigeria'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Nigeria

all_data = []
for params['page'] in range(1, Nigeria_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[271]:


#Brazil
country = 'Brazil'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Brazil

all_data = []
for params['page'] in range(1, Brazil_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[272]:


#Netherlands
country = 'Netherlands'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Netherlands

all_data = []
for params['page'] in range(1, Netherlands_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[273]:


#Saudi_Arabia
country = 'Saudi_Arabia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Saudi_Arabia

all_data = []
for params['page'] in range(1, Saudi_Arabia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[274]:


#Czech_Republic
country = 'Czech_Republic'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Czech_Republic

all_data = []
for params['page'] in range(1, Czech_Republic_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[275]:


#Slovenia
country = 'Slovenia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Slovenia

all_data = []
for params['page'] in range(1, Slovenia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[276]:


#United_Arab_Emirates
country = 'United_Arab_Emirates'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = United_Arab_Emirates

all_data = []
for params['page'] in range(1, United_Arab_Emirates_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[277]:


#Lebanon
country = 'Lebanon'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Lebanon

all_data = []
for params['page'] in range(1, Lebanon_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[278]:


#New_Zealand
country = 'New_Zealand'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = New_Zealand

all_data = []
for params['page'] in range(1, New_Zealand_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[279]:


#Liechtenstein
country = 'Liechtenstein'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Liechtenstein

all_data = []
for params['page'] in range(1, Liechtenstein_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[280]:


#Kenya
country = 'Kenya'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Kenya

all_data = []
for params['page'] in range(1, Kenya_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[281]:


#Latvia
country = 'Latvia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Latvia

all_data = []
for params['page'] in range(1, Latvia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[282]:


#Tunisia
country = 'Tunisia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Tunisia

all_data = []
for params['page'] in range(1, Tunisia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[283]:


#Argentina
country = 'Argentina'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Argentina

all_data = []
for params['page'] in range(1, Argentina_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[284]:


#Bermuda
country = 'Bermuda'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Bermuda

all_data = []
for params['page'] in range(1, Bermuda_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[285]:


#Malaysia
country = 'Malaysia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Malaysia

all_data = []
for params['page'] in range(1, Malaysia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[286]:


#Panama
country = 'Panama'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Panama

all_data = []
for params['page'] in range(1, Panama_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[287]:


#Sweden
country = 'Sweden'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Sweden

all_data = []
for params['page'] in range(1, Sweden_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[288]:


#Cyprus
country = 'Cyprus'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Cyprus

all_data = []
for params['page'] in range(1, Cyprus_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[289]:


#Ghana
country = 'Ghana'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Ghana

all_data = []
for params['page'] in range(1, Ghana_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[290]:


#Iraq
country = 'Iraq'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Iraq

all_data = []
for params['page'] in range(1, Iraq_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[291]:


#Mauritius
country = 'Mauritius'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Mauritius

all_data = []
for params['page'] in range(1, Mauritius_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[292]:


#Bahrain
country = 'Bahrain'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Bahrain

all_data = []
for params['page'] in range(1, Bahrain_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[293]:


#Egypt
country = 'Egypt'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Egypt

all_data = []
for params['page'] in range(1, Egypt_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[294]:


#Thailand
country = 'Thailand'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Thailand

all_data = []
for params['page'] in range(1, Thailand_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[295]:


#Bangladesh
country = 'Bangladesh'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Bangladesh

all_data = []
for params['page'] in range(1, Bangladesh_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[296]:


#Ivory_Coast
country = 'Ivory_Coast'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Ivory_Coast

all_data = []
for params['page'] in range(1, Ivory_Coast_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[297]:


#Indonesia
country = 'Indonesia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Indonesia

all_data = []
for params['page'] in range(1, Indonesia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[298]:


#Iceland
country = 'Iceland'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Iceland

all_data = []
for params['page'] in range(1, Iceland_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[299]:


#Jordan
country = 'Jordan'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Jordan

all_data = []
for params['page'] in range(1, Jordan_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[300]:


#Mozambique
country = 'Mozambique'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Mozambique

all_data = []
for params['page'] in range(1, Mozambique_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[301]:


#Poland
country = 'Poland'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Poland

all_data = []
for params['page'] in range(1, Poland_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[302]:


#Tanzania
country = 'Tanzania'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Tanzania

all_data = []
for params['page'] in range(1, Tanzania_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[303]:


#Cameroon
country = 'Cameroon'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Cameroon

all_data = []
for params['page'] in range(1, Cameroon_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[304]:


#Kuwait
country = 'Kuwait'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Kuwait

all_data = []
for params['page'] in range(1, Kuwait_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[305]:


#Libya
country = 'Libya'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Libya

all_data = []
for params['page'] in range(1, Libya_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[306]:


#Malta
country = 'Malta'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Malta

all_data = []
for params['page'] in range(1, Malta_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[307]:


#Mexico
country = 'Mexico'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Mexico

all_data = []
for params['page'] in range(1, Mexico_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[308]:


#Oman
country = 'Oman'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Oman

all_data = []
for params['page'] in range(1, Oman_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[309]:


#Pakistan
country = 'Pakistan'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Pakistan

all_data = []
for params['page'] in range(1, Pakistan_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[310]:


#Uganda
country = 'Uganda'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Uganda

all_data = []
for params['page'] in range(1, Uganda_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[311]:


#Venezuela
country = 'Venezuela'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Venezuela

all_data = []
for params['page'] in range(1, Venezuela_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[312]:


#Kosovo
country = 'Kosovo'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Kosovo

all_data = []
for params['page'] in range(1, Kosovo_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[313]:


#Angola
country = 'Angola'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Angola

all_data = []
for params['page'] in range(1, Angola_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[314]:


#Burkina_Faso
country = 'Burkina_Faso'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Burkina_Faso

all_data = []
for params['page'] in range(1, Burkina_Faso_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[315]:


#Botswana
country = 'Botswana'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Botswana

all_data = []
for params['page'] in range(1, Botswana_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[316]:


#Congo
country = 'Congo'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Congo

all_data = []
for params['page'] in range(1, Democratic_Republic_Of_The_Congo_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[317]:


#Guatemala
country = 'Guatemala'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Guatemala

all_data = []
for params['page'] in range(1, Guatemala_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[318]:


#Jamaica
country = 'Jamaica'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Jamaica

all_data = []
for params['page'] in range(1, Jamaica_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[319]:


#Cayman_Islands
country = 'Cayman_Islands'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Cayman_Islands

all_data = []
for params['page'] in range(1, Cayman_Islands_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[320]:


#Madagascar
country = 'Madagascar'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Madagascar

all_data = []
for params['page'] in range(1, Madagascar_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[321]:


#Macedonia
country = 'Macedonia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Macedonia

all_data = []
for params['page'] in range(1, Former_Yugoslav_Republic_Of_Macedonia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[322]:


#Maldives
country = 'Maldives'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Maldives

all_data = []
for params['page'] in range(1, Maldives_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[323]:


#Namibia
country = 'Namibia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Namibia

all_data = []
for params['page'] in range(1, Namibia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[324]:


#Niger
country = 'Niger'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Niger

all_data = []
for params['page'] in range(1, Niger_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[325]:


#Peru
country = 'Peru'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Peru

all_data = []
for params['page'] in range(1, Peru_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[326]:


#Qatar
country = 'Qatar'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Qatar

all_data = []
for params['page'] in range(1, Qatar_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[327]:


#Slovakia
country = 'Slovakia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Slovakia

all_data = []
for params['page'] in range(1, Slovakia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[328]:


#Togo
country = 'Togo'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Togo

all_data = []
for params['page'] in range(1, Togo_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[329]:


#Trinidad_and_Tobago
country = 'Trinidad_and_Tobago'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Trinidad_and_Tobago

all_data = []
for params['page'] in range(1, Trinidad_and_Tobago_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[330]:


#Andorra
country = 'Andorra'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Andorra

all_data = []
for params['page'] in range(1, Andorra_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[331]:


#Antigua_and_Barbuda
country = 'Antigua_and_Barbuda'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Antigua_and_Barbuda

all_data = []
for params['page'] in range(1, Antigua_and_Barbuda_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[332]:


#Albania
country = 'Albania'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Albania

all_data = []
for params['page'] in range(1, Albania_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[333]:


#Barbados
country = 'Barbados'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Barbados

all_data = []
for params['page'] in range(1, Barbados_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[334]:


#Benin
country = 'Benin'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Benin

all_data = []
for params['page'] in range(1, Benin_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[335]:


#Bolivia
country = 'Bolivia'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Bolivia

all_data = []
for params['page'] in range(1, Bolivia_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[336]:


#Bahamas
country = 'Bahamas'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Bahamas

all_data = []
for params['page'] in range(1, Bahamas_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[337]:


#Central_African
country = 'Central_African'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Central_African

all_data = []
for params['page'] in range(1, Central_African_Republic_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[338]:


#Djibouti
country = 'Djibouti'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Djibouti

all_data = []
for params['page'] in range(1, Djibouti_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[339]:


#Algeria
country = 'Algeria'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Algeria

all_data = []
for params['page'] in range(1, Algeria_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[340]:


#Ecuador
country = 'Ecuador'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Ecuador

all_data = []
for params['page'] in range(1, Ecuador_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[341]:


#Gibraltar
country = 'Gibraltar'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Gibraltar

all_data = []
for params['page'] in range(1, Gibraltar_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[342]:


#Guam
country = 'Guam'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Guam

all_data = []
for params['page'] in range(1, Guam_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[343]:


#Haiti
country = 'Haiti'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Haiti

all_data = []
for params['page'] in range(1, Haiti_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[344]:


#Sri_Lanka
country = 'Sri_Lanka'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Sri_Lanka

all_data = []
for params['page'] in range(1, Sri_Lanka_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[345]:


#Macao
country = 'Macao'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Macao

all_data = []
for params['page'] in range(1, Macao_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[346]:


#Mauritania
country = 'Mauritania'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Mauritania

all_data = []
for params['page'] in range(1, Mauritania_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[347]:


#Nicaragua
country = 'Nicaragua'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Nicaragua

all_data = []
for params['page'] in range(1, Nicaragua_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[348]:


#Nepal
country = 'Nepal'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Nepal

all_data = []
for params['page'] in range(1, Nepal_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[349]:


#Rwanda
country = 'Rwanda'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Rwanda

all_data = []
for params['page'] in range(1, Rwanda_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[350]:


#El_Salvador
country = 'El_Salvador'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = El_Salvador

all_data = []
for params['page'] in range(1, El_Salvador_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[351]:


#Chad
country = 'Chad'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Chad

all_data = []
for params['page'] in range(1, Chad_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[352]:


#Taiwan
country = 'Taiwan'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = Taiwan

all_data = []
for params['page'] in range(1, Taiwan_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[353]:


#British_Virgin_Islands
country = 'British_Virgin_Islands'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {'page': 1}
url = British_Virgin_Islands

all_data = []
for params['page'] in range(1, British_Virgin_Islands_pages):  # <-- increase number of pages here
    print('Page {}...'.format(params['page']))
    soup = BeautifulSoup(requests.get(url, headers=headers, params=params).content, 'html.parser')

    # remove unnecessary information:
    for t in soup.select('.show-mobile'):
        t.extract()

    for c1, c2, c3 in zip(soup.select('#companyResults .col-md-6')[1:],
                        soup.select('#companyResults .col-md-4')[1:],
                        soup.select('#companyResults .col-md-2')[1:]):
        all_data.append({
            'Name': c1.get_text(strip=True),
            'Location': ' '.join(c2.get_text(strip=True).split()),
            'Revenue': c3.get_text(strip=True)
        })
    
df = pd.DataFrame(all_data)
df.to_csv(country+'.csv')
# print(df)


# In[354]:


China_pages = 187
Spain_pages = 168
Italy_pages = 72
United_Kingdom_pages = 66
Morocco_pages = 58
United_States_pages = 52
Colombia_pages = 47
Israel_pages = 25
Switzerland_pages = 12
Finland_pages = 11
Russian_Federation_pages = 10
Uzbekistan_pages = 9
Austria_pages = 7
Hong_Kong_pages = 7
Denmark_pages = 6
Republic_Of_Korea_pages = 5
Australia_pages = 5
Belgium_pages = 4
India_pages = 4
Ireland_pages = 4
Japan_pages = 3
Singapore_pages = 3
Germany_pages = 3
Vietnam_pages = 2
Portugal_pages = 2

France_pages = 2
Greece_pages = 2
South_Africa_pages = 2
Hungary_pages = 2
Chile_pages = 2
Bulgaria_pages = 2
Canada_pages = 2
Turkey_pages = 2

Romania_pages = 2
Croatia_pages = 2
Estonia_pages = 2
Philippines_pages = 2
Serbia_pages = 2
Luxembourg_pages = 2
Bosnia_Herzegovina_pages = 2
Nigeria_pages = 2
Brazil_pages = 2

Netherlands_pages = 2
Saudi_Arabia_pages = 2
Czech_Republic_pages = 2
Slovenia_pages = 2
United_Arab_Emirates_pages = 2
Lebanon_pages = 2
New_Zealand_pages = 2
Liechtenstein_pages = 2
Kenya_pages = 2

Latvia_pages = 2
Tunisia_pages = 2
Argentina_pages = 2
Bermuda_pages = 2
Malaysia_pages = 2
Panama_pages = 2
Sweden_pages = 2

Cyprus_pages = 2
Ghana_pages = 2
Iraq_pages = 2
Mauritius_pages = 2
Bahrain_pages = 2
Egypt_pages = 2
Thailand_pages = 2

Bangladesh_pages = 2
Ivory_Coast_pages = 2
Indonesia_pages = 2
Iceland_pages = 2
Jordan_pages = 2
Mozambique_pages = 2
Poland_pages = 2
Tanzania_pages = 2

Cameroon_pages = 2
Kuwait_pages = 2
Libya_pages = 2
Malta_pages = 2
Mexico_pages = 2
Oman_pages = 2
Pakistan_pages = 2

Uganda_pages = 2
Venezuela_pages = 2
Kosovo_pages = 2
Angola_pages = 2
Burkina_Faso_pages = 2
Botswana_pages = 2

Democratic_Republic_Of_The_Congo_pages = 2
Guatemala_pages = 2
Jamaica_pages = 2
Cayman_Islands_pages = 2
Madagascar_pages = 2

Former_Yugoslav_Republic_Of_Macedonia_pages = 2
Maldives_pages = 2
Namibia_pages = 2
Niger_pages = 2
Peru_pages = 2

Qatar_pages = 2
Slovakia_pages = 2
Togo_pages = 2
Trinidad_and_Tobago_pages = 2
Andorra_pages = 2
Antigua_and_Barbuda_pages = 2
Albania_pages = 2

Barbados_pages = 2
Benin_pages = 2
Bolivia_pages = 2
Bahamas_pages = 2
Central_African_Republic_pages = 2
Djibouti_pages = 2

Algeria_pages = 2
Ecuador_pages = 2
Gibraltar_pages = 2
Guam_pages = 2

Haiti_pages = 2
Sri_Lanka_pages = 2
Macao_pages = 2
Mauritania_pages = 2
Nicaragua_pages = 2

Nepal_pages = 2
Rwanda_pages = 2
El_Salvador_pages = 2
Chad_pages = 2
Taiwan_pages = 2
British_Virgin_Islands_pages = 2


# In[180]:


#links
China = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.cn.html'
Spain = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.es.html'
Italy = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.it.html'
United_Kingdom = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.gb.html'
Morocco = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ma.html'
United_States = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.us.html'
Colombia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.co.html'
Israel = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.il.html'
Switzerland = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ch.html'
Finland = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.fi.html'
Russian_Federation = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ru.html'
Uzbekistan = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.uz.html'
Austria = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.at.html'
Hong_Kong = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.hk.html'
Denmark = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.dk.html'
Republic_Of_Korea = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.kr.html'
Australia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.au.html'
Belgium = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.be.html'
India = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.in.html'
Ireland = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ie.html'
Japan = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.jp.html'
Singapore = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.sg.html'
Germany = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.de.html'
Vietnam = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.vn.html'
Portugal = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.pt.html'
France = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.fr.html'
Greece = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.gr.html'
South_Africa = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.za.html'
Hungary = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.hu.html'
Chile = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.cl.html'
Bulgaria = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bg.html'
Canada = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ca.html'
Turkey = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.tr.html'
Romania = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ro.html'
Croatia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.hr.html'
Estonia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ee.html'
Philippines = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ph.html'
Serbia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.rs.html'
Luxembourg = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.lu.html'
Bosnia_Herzegovina = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ba.html'
Nigeria = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ng.html'
Brazil = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.br.html'
Netherlands = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.nl.html'
Saudi_Arabia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.sa.html'
Czech_Republic = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.cz.html'
Slovenia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.si.html'
United_Arab_Emirates = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ae.html'
Lebanon = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.lb.html'
New_Zealand = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.nz.html'
Liechtenstein = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.li.html'
Kenya = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ke.html'
Latvia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.lv.html'
Tunisia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.tn.html'
Argentina = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ar.html'
Bermuda = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bm.html'
Malaysia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.my.html'
Panama = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.pa.html'
Sweden = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.se.html'
Cyprus = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.cy.html'
Ghana = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.gh.html'
Iraq = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.iq.html'
Mauritius = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.mu.html'
Bahrain = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bh.html'
Egypt = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.eg.html'
Thailand = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.th.html'
Bangladesh = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bd.html'
Ivory_Coast = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ci.html'
Indonesia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.id.html'
Iceland = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.is.html'
Jordan = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.jo.html'

Mozambique = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.mz.html'
Poland = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.pl.html'
Tanzania = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.tz.html'
Cameroon = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.cm.html'
Kuwait = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.kw.html'
Libya = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ly.html'
Malta = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.mt.html'
Mexico = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.mx.html'
Oman = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.om.html'
Pakistan = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.pk.html'

Uganda = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ug.html'
Venezuela = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ve.html'
Kosovo = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.xk.html'
Angola = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ao.html'
Burkina_Faso = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bf.html'
Botswana = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bw.html'
Congo = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.cd.html'

Guatemala = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.gt.html'
Jamaica = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.jm.html'
Cayman_Islands = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ky.html'
Madagascar = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.mg.html'

Macedonia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.mk.html'
Maldives = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.mv.html'
Namibia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.na.html'
Niger = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ne.html'
Peru = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.pe.html'

Qatar = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.qa.html'
Slovakia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.sk.html'
Togo = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.tg.html'
Trinidad_and_Tobago = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.tt.html'
Andorra = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ad.html'
Antigua_and_Barbuda = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ag.html'
Albania = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.al.html'

Barbados = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bb.html'
Benin = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bj.html'
Bolivia = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bo.html'
Bahamas = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.bs.html'
Central_African = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.cf.html'
Djibouti = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.dj.html'

Algeria = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.dz.html'
Ecuador = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ec.html'
Gibraltar = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.gi.html'
Guam = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.gu.html'

Haiti = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ht.html'
Sri_Lanka = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.lk.html'
Macao = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.mo.html'
Mauritania = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.mr.html'
Nicaragua = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.ni.html'

Nepal = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.np.html'
Rwanda = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.rw.html'
El_Salvador = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.sv.html'
Chad = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.td.html'
Taiwan = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.tw.html'
British_Virgin_Islands = 'https://www.dnb.com/business-directory/company-information.insurance-carriers.vg.html'


# In[97]:


country_list = [#'China','Spain','Italy','United_Kingdom','Morocco',
                'United_States','Colombia','Israel_ur','Switzerland','Finland','Russian_Federation','Uzbekistan','Austria','Hong_Kong','Denmark','Republic_Of_Korea','Australia','Belgium','India','Ireland','Japan','Singapore','Germany','Vietnam','Portugal','France','Greece','South_Africa','Hungary','Chile','Bulgaria','Canada','Turkey','Romania','Croatia','Estonia','Philippines','Serbia','Luxembourg','Bosnia_Herzegovina','Nigeria','Brazil','Netherlands','Saudi_Arabia','Czech_Republic','Slovenia','United_Arab_Emirates','Lebanon','New_Zealand','Liechtenstein','Kenya','Latvia','Tunisia','Argentina','Bermuda','Malaysia','Panama','Sweden','Cyprus','Ghana','Iraq','Mauritius','Bahrain','Egypt','Thailand','Bangladesh','Ivory_Coast','Indonesia','Iceland','Jordan','Mozambique','Poland','Tanzania','Cameroon','Kuwait','Libya','Malta','Mexico','Oman','Pakistan','Uganda','Venezuela','Kosovo','Angola','Burkina_Faso','Botswana','Congo','Guatemala','Jamaica','Cayman_Islands','Madagascar','Macedonia','Maldives','Namibia','Niger','Peru','Qatar','Slovakia','Togo','Trinidad_and_Tobago','Andorra','Antigua_and_Barbuda','Albania','Barbados','Benin','Bolivia','Bahamas','Central_African','Djibouti','Algeria','Ecuador','Gibraltar','Guam','Haiti','Sri_Lanka','Macao','Mauritania','Nicaragua','Nepal','Rwanda','El_Salvador','Chad','Taiwan','British_Virgin_Islands']


# In[470]:


#merge all csvs
path = r'C:\Users\maxwell.bade\Downloads\Highmark\andi\test'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)


frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv('insurance_rev_country.csv')

#keep only interesting columns
df = frame[['Name','Location','Revenue']]

#remove unwanted characters
df['Revenue'] = df['Revenue'].str.replace(r'M', '')
df['Revenue'] = df['Revenue'].str.replace(r'$', '')
df['Revenue'] = df['Revenue'].str.replace(r',', '')
df['Revenue'] = df.Revenue.astype(float)

#add country column
df['Country'] = df['Location'].str.rsplit(',').str[-1]

#rename cols
df.columns = ['Name','Location','Revenue(in Millions)','Country']

df.to_csv('insurance_rev_country.csv')


# In[469]:


df


# In[ ]:




