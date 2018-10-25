"""Configuration file for the website. Fill out all the information."""

# background banner
bg_banner = './img/banner_cut.jpg'

# contact info
gs_name = ('Nickalas Reynolds', 'nickreynolds@ou.edu')
gs_pict = './img/oulogo.png'
group = 'Star Formation || Proto&#8209;multiple Evolution'
advisor = ['Nathan Kaib', 'https://nhn.ou.edu/~kaib']
phone = '0000000000'
office = '405'
lab = ''
social_media = {
    'twitte': '',
    'instagram': '',
    'linkedin': '',
    'github': 'nickalaskreynolds',
    'facebook': '',
    'reddit': '',
}

# link to CV
cv = 'https://www.nhn.ou.edu/~reynolds/public_files/spf2poster.pdf'

# papers/reports/conferences
papers = (('Ro-vib. OH Emission HAEBEs',
          'http://adsabs.harvard.edu/abs/2016ApJ...830..112B'), )

# For populating the carousel
hightlights = ()

"""For all below sections, urls and images are supported separately.
urls follow this format <<url>>||name|| .
images follow this format {{url}}[[name]]--width x height--
examples: <<randomUrl>>||urlName|| {{image url}}[[name]]--100px x 100px--"""

pages = {
    # Home Page section. Each '': designates the section title
    # and everything after : is in section. Images/urls are supported
    'home': {
        'Splash': 'My name is Nickalas Reynolds. I am a second yea' +
        ' graduate assistant at the University of Oklahoma. I spend ' +
        'most of my time analyzing data retrieved by ' +
        '<<https://science.nrao.edu/facilities/alma>>||ALMA||' +
        ' and working on the ' +
        ' <<https://nhn.ou.edu/~srt>>||Sooner Radio Telescope||' +
        ' hosted by the University of Oklahoma on top of Nielsen Hall.',

        'Research': 'My current research focuses on the formation and ' +
        'evolution of YSOs and understanding the nature of stellar ' +
        'multiplicities and formation of proto-stellar disks. We focus' +
        ' on dense star forming regions like that of Perseus and Orion.' +
        '{{./img/l1448.jpg}}[[L1448N]]--500px x 500px--',
    },

    # About me section. Each '': designates the section title
    # and everything after : is in section. Images/urls are supported
    'about_me': {
        'Hobbies': 'Some hobbies that I enjoy are: learning new coding' +
        ' languages (and implementing them), maintaining servers, and ' +
        'imaging astronomical objects on the <<http://observatory.ou.edu>>' +
        '||16 inch telescope||, like the {{./img/ringnebula.jpg}}' +
        '[[Ring Nebula]]--600px x 600px--',
        'Background': 'I went to Clemson University for my Bachelors degree' +
        'in Physics (\'16) and am currently attending the University of ' +
        'Oklahoma for my Ph.D. in Astronomy. ',
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
