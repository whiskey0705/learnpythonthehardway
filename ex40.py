class Song(object):  
# 为什么class定义的时候只能传入object或者不传，其他值都出错？
# python旧版本里是不用传object的，但是发现有缺陷，所有添加了关键词

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(['Happy birthday to you',
                    'I don\'t want to get sued', 
                    'So I\'ll stop right there'])


bulls_on_parade = Song(['They rally around tha family',
                        'With pockets full of shells'])

happy_bday.sing_me_a_song()


bulls_on_parade.sing_me_a_song()