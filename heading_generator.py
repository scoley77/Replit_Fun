def heading_generator(title, type):
  heading = f'<h{type}>{title}</h{type}>'
  return heading

print(heading_generator('hello', '1'))