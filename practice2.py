import pyhtml as h
t = h.html(
     h.head(
         h.title('test page')
     ),
     h.body(
         h.h1("this is the title"),
         h.div("this is some text"),
         h.div(h.h2("inside html"),
               h.p("this is inner para")
            )
     )
 )
print(t.render())



