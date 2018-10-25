"""Configuration file for the website. Fill out all the information."""

# background banner
bg_banner = './img/banner_cut.jpg'

# contact info
gs_name = ('Example', 'exampleemail@ou.edu')
gs_pict = ''
group = ''
advisor = ('Example', 'exampleemail@ou.edu')
phone = ''
office = ''
lab = ''

# link to CV
cv = ''

"""For all below sections, urls and images are supported separately.
urls follow this format <<url>>||name|| .
images follow this format {{url}}[[name]]--width x height--
examples: <<randomUrl>>||urlName|| {{image url}}[[name]]--100px x 100px--"""

pages = {
    # Home Page section. Each '': designates the section title
    # and everything after : is in section. Images/urls are supported
    'home': {
        'Section 1': 'Some stuff in here {{./img/oulogo.png}}[[name]]' +
        '<<randomUrl>>||urlName||',
        'Section 2': 'Some stuff in here {{./img/oulogo.png}}[[name]]' +
        '<<randomUrl>>||urlName||',
    },

    # About me section. Each '': designates the section title
    # and everything after : is in section. Images/urls are supported
    'about_me': {
        'Section 1': 'Some stuff in here {{./img/oulogo.png}}[[name]]' +
        '<<randomUrl>>||urlName||',
        'Section 2': 'Some stuff in here {{./img/oulogo.png}}[[name]]' +
        '<<randomUrl>>||urlName||',
    },

    # Research section. Each '': designates the section title
    # and everything after : is in section. Images/urls are supported
    'research': {
        'Section 1': 'Some stuff in here {{./img/oulogo.png}}[[name]]' +
        '<<randomUrl>>||urlName||',
        'Section 2': 'Some stuff in here {{./img/oulogo.png}}[[name]]' +
        '<<randomUrl>>||urlName||',
    },

    # Teaching section. Each '': designates the section title
    # and everything after : is in section. Images/urls are supported
    'teaching': {
        'Section 1': 'Some stuff in here {{./img/oulogo.png}}[[name]]' +
        '<<randomUrl>>||urlName||',
        'Section 2': 'Some stuff in here {{./img/oulogo.png}}[[name]]' +
        '<<randomUrl>>||urlName||',
    },

    # Projects section. Each '': designates the section title
    # and everything after : is in section. Images/urls are supported
    'projects': {},

    # Contact section. Each '': designates the section title
    # and everything after : is in section. Images/urls are supported
    'contact': {},

}
# end of file
