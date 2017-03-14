from wordcloud import WordCloud, ImageColorGenerator
import jieba
from os import path
from scipy.misc import imread
from sys import argv

script, input_file, mask_image = argv
d = path.dirname(__file__)

# Read the whole text
text_from_file_with_apath = open(input_file).read() 

# read the mask image / color image
mask_coloring = imread(path.join(d, mask_image))
 
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True) 
wl_space_split = " ".join(wordlist_after_jieba) 

# wordcloud本身的字库不支持中文显示，这里用文件夹里的字库替换以支持中文
font = path.join(d, "DroidSansFallbackFull.ttf")

wc = WordCloud(background_color="white", max_words=2000, mask=mask_coloring, font_path=font)

# generate word cloud
wc.generate(wl_space_split)

# create coloring from image
image_colors = ImageColorGenerator(mask_coloring)

# store to file
# store a default color to file 'wordclound.png'
wc.to_file(path.join(d, "wordcloud.png"))

# store a color according to color provided by image to file 'recoloring_wordcloud.png'
wc.recolor(color_func=image_colors)
wc.to_file(path.join(d, "recoloring_wordcloud.png"))
