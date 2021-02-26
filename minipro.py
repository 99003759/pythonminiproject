import re


# searching class
class search_word:
    def search_function(self, search_word):
        # searching function for given word
        self.search_word = search_word
        # opening the file
        file_open = open("input.txt", 'rt')
        # reading the file
        content = file_open.read()
        # searing the word
        word_found = re.findall(search_word, content, re.M | re.I)
        one_num = 0
        store_word = []
        store_span = 0
        # code to add the before and after words of searing word
        while one_num < len(word_found):
            # first searching word code
            if one_num == 0:
                word_got = re.search(word_found[one_num], content)
                one_num = one_num + 1
                get_span = word_got.span()
                store_span = get_span[1]
                store_word.append(content[get_span[0]-10:get_span[0]] + ' ' +
                                  search_word + ' ' +
                                  content[get_span[1]+1:get_span[1]+10])
            # after first word                      
            else:
                word_got = re.search(word_found[one_num],
                                     content[store_span+1:])
                one_num = one_num + 1
                get_span = word_got.span()
                store_span = get_span[1]
                store_word.append(content[get_span[0]-10:get_span[0]]+' ' +
                                  search_word + ' ' +
                                  content[get_span[1]+1:get_span[1]+10])
        conv_str = []
        # converion of no of words into string and added
        conv_str.append(str(len(word_found)))
        # converting the words into single line each
        for y in range(1, len(store_word)+1):
            conv_str.append(str(y) + ": " + store_word[y-1].strip())
        # creating the name of output file
        out_txt = search_word + ".txt"
        # appending the lines into the file
        with open(out_txt, 'a') as file_out:
            file_out.writelines('\n'.join(conv_str))
if __name__ == "__main__":
    # main function
    object_search = search_word()
    search_word = input("enter search word: ")
    object_search.search_function(search_word)
