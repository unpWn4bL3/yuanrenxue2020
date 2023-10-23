# from fontTools.ttLib import TTFont
# from PIL import Image, ImageDraw, ImageFont

# # 替换为您的.ttf文件路径
# font_path = "download.ttf"

# # 定义字体大小
# font_size = 200

# # 加载TrueType字体
# font = TTFont(font_path)

# # 获取所有字形的数量
# num_glyphs = len(font["glyf"].glyphs)

# # 循环绘制每个字形
# for i in range(num_glyphs):
#     char = chr(i) if i >= 32 else f"Glyph_{i}"

#     # 创建一个新的Image对象
#     char_image = Image.new("RGB", (font_size, font_size), "black")
#     char_draw = ImageDraw.Draw(char_image)

#     # 加载字体并在新的Image对象上绘制字符
#     font = ImageFont.truetype(font_path, font_size)
#     char_draw.text((0, 0), char, font=font, fill="white")

#     # 保存图像
#     char_image.save(f"glyph_{i}.png")

# # 请注意：这将在当前目录下生成多个图像文件，分别对应每个字形。

from fontTools.ttLib import TTFont

fontpath = "./download.ttf"

font = TTFont(fontpath)
# font_dict = font.getBestCmap()

font.saveXML("./a.xml")
# pass
