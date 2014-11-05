Title: Markdown syntax recap
Tags: markdown
Date: 2013-4-02


From the [original markdown syntax post](http://daringfireball.net/projects/markdown/syntax). With sections abbreviated and reordered.

# Quick ref

    [link text](http://example.net/)
    ![alt text](/path/to/img.jpg)
    *  list
    ## h2 heading


### Pelican specific

    [a link relative to content root](|filename|python-one-of-natures-giants.md)
    ![alt text](|filename|/images/autosave.jpeg)


# Full ref

## Links

    [This link](http://example.net/)
    [an example](http://example.com/ &quot;Title&quot;)

    [About](/about/)

    This is [an example][id] reference-style link.
    [id]: http://example.com/  &quot;Optional Title Here&quot;

    [Google][]
    [Google]: http://google.com/


## Images

    ![Alt text](/path/to/img.jpg)
    ![Alt text](/path/to/img.jpg &quot;Optional title&quot;)

    ![Alt text][id]
    [id]: url/to/image  &quot;Optional title attribute&quot;


## Codeblock

    `:::javascript`
    tell application &quot;Foo&quot;
        beep
    end tell


## Code

    Please do not use any `<blink>` tags.


## Lists

    *   Red
    +   Green
    -   Blue
    1.  Bird
    2.  McHale
        indented part of #2


## Headings

# H1

## H2

### H3

#### H4

##### H5

###### H6

    This is an H1
    =============
    This is an H2
    -------------

    # This is an H1
    ## This is an H2 ##
    ### This is an H3 ######


## Blockquotes

    &gt; This is the first level of quoting.
    &gt;
    &gt; &gt; This is nested blockquote.


## Horizontal rule

    * * * / *** / ***** / - - -
    ---------------------------------------


## Emphasis

    *single asterisks*
    _single underscores_
    **double asterisks**
    __double underscores__


    _1 star_ **2 stars** _1 underscore_ **2 underscores**

## Backslash escapes

    \   backslash
    `   backtick
    *   asterisk
    _   underscore
    {}  curly braces
    []  square brackets
    ()  parentheses
    #   hash mark
    +   plus sign
    -   minus sign (hyphen)
    .   dot
    !   exclamation mark
