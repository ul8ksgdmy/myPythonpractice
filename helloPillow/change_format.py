# from PIL import Image
# # with Image.open('helloPillow/python.png') as im:
#     # im.save('helloPillow/python_quality_40.jpg') #quality는 jpg만 유효
#     # 에러 발생 원인은 https://github.com/python-pillow/Pillow/issues/2609 참고
# # with open('test.txt', 'wt') as f:
# #     f.write('abc')

# # with Image.open('helloPillow/python.png') as im:
# #     with Image.new('RGBA', im.size, (255,255,255)) as canvas:
# #         merged_im = Image.alpha_composite(canvas, im)
# #         merged_im.save('python_bg_white.jpg')
# # 같은 이유로 에러

# with Image.open('helloPillow/python.png') as im:
#     im.thumbnail((300,300))
#     im.save('helloPillow/python_300_300.png')