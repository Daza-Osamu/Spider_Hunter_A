import turtle
import random
import time
oyuncu_skoru = 0
orumcek_skoru = 0

spider = turtle.Turtle()

ses = turtle.Turtle()
ses.hideturtle()
ses.penup()
ses.goto(0,-300)

timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(-500, 350)


hud = turtle.Turtle()
hud.hideturtle()
hud.penup()
hud.goto(30, 350)


turtle_screen = turtle.Screen()

turtle.title("Spider Demo")
turtle_screen.register_shape("spider.gif")
spider.shape("spider.gif")
spider.penup()
spider.speed(0)

secilecek_renk = turtle_screen.textinput("renk seçimi","lütfen renginizi hex kodu olarak giriniz:")
turtle_screen.bgcolor(secilecek_renk)




secilen_dakika = turtle_screen.numinput("Süre Seçimi", "Kaç dakika hayatta kalabilirsin? (2-5 arası):")
if secilen_dakika is None:
    secilen_dakika = 0
if secilen_dakika >= 0 and secilen_dakika < 2:
    spider.hideturtle()
    ses.write("Bazen en dogrusu hiç savasa girmemektir.", align="center",font=("Courier", 30, "bold"))
    turtle.done()
elif secilen_dakika > 5:
    ses.write("Bana karsi hic sansin yok ! - Yenildin.", align="center",font=("Courier", 30, "bold"))
    turtle.done()
elif secilen_dakika >= 2 and secilen_dakika <= 5:
    kalan_saniye = int(secilen_dakika * 60)

def geri_sayim():
    global kalan_saniye
    dakika = kalan_saniye // 60
    saniye = kalan_saniye % 60

    timer.clear()
    timer.write(f"Kalan zaman:{dakika}.{saniye}", align="center", font=("Courier", 30, "bold"))
    if kalan_saniye > 0:
       kalan_saniye -= 1
       turtle_screen.ontimer(geri_sayim, 1000)

    else:
        timer.clear()
        if oyuncu_skoru > orumcek_skoru:
            hud.write(f"Yasamayi hak ettin.P:{oyuncu_skoru}S:{orumcek_skoru}", align="center", font=("Courier", 30, "bold"))
            turtle.done()
        elif oyuncu_skoru < orumcek_skoru:
            hud.write(f"Adil bir savas olmadigini soylemistim.P:{oyuncu_skoru}S:{orumcek_skoru}", align="center", font=("Courier", 30, "bold"))
            turtle.done()
        elif oyuncu_skoru == orumcek_skoru:
            hud.write(f"Bu gun sansli gunundesin.P:{oyuncu_skoru}S:{orumcek_skoru}", align="center", font=("Courier", 30, "bold"))
            turtle.done()

geri_sayim()


fare_x = 0
fare_y = 0
def imlec_takip(event):
    global fare_x, fare_y

    fare_x = event.x - (turtle_screen.window_width() / 2)
    fare_y = (turtle_screen.window_height() / 2) - event.y

canvas = turtle_screen.getcanvas()

canvas.bind('<Motion>', imlec_takip)

spider.hideturtle()


def orumcek_saldirisi():
    global oyuncu_skoru, orumcek_skoru
    # 1. Örümcek ışınlanır ve ekranda belirir
    spider.goto(fare_x, fare_y)
    spider.showturtle()

    # 2. KRİTİK DÜZELTME: 1 Saniye sonra GİZLENME komutu (Kendini çağırmaz!)
    turtle_screen.ontimer(spider.hideturtle, 1000)

    # 3. 3 ile 8 saniye arası rastgele pusu süresi
    Bekleme_suresi = random.randint(3000, 15000)

    # 4. Pusudan sonra tekrar saldır!
    turtle_screen.ontimer(orumcek_saldirisi, Bekleme_suresi)
    mesafe = spider.distance(fare_x, fare_y)
    if mesafe < 50:
        ses.clear()
        ses.write(f"Benden Kaçamazsin! Mesafe: {mesafe:.0f} pixel - Yenildin!", align="center", font=("Courier", 30, "bold"))
        orumcek_skoru += 1
    else:
        ses.clear()
        ses.write("Bir dahakine bu kadar sansli olamayacaksin!", align="center", font=("Courier", 30, "bold"))
        oyuncu_skoru += 1
orumcek_saldirisi()
turtle.mainloop()