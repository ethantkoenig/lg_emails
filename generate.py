#! /usr/bin/python3

import jinja2
import sys

def main():
  env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
  template = env.get_template(sys.argv[1])
  print(template.render())


if __name__ == '__main__':
  main()
