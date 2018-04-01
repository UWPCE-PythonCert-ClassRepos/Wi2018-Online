#!/usr/local/opt/coreutils/libexec/gnubin/env python3


def reverse_word(word):
    if word:
        return word[-1] + reverse_word(word[:-1])
    else:
        return ''


def main():
    print(reverse_word("Michael"))  # There's no need for the intermidiary


if __name__ == "__main__":
    main()
