"""Builds ar/index.html from index.html.

ar/index.html is generated, never hand-edited. Every swap asserts its
expected hit count, so a string that drifts in the English file fails the
build here instead of silently shipping English text on the Arabic page.

Run after any edit to index.html:  python3 tools/make-ar.py
Paths resolve from this file, so the working directory does not matter.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "index.html"
DST = ROOT / "ar" / "index.html"

R = []


def sub(old, new, n=1):
    R.append((old, new, n))


# ── head ──────────────────────────────────────────────────────────
sub('<html lang="en" dir="ltr">', '<html lang="ar" dir="rtl">')
sub('<title>Padel Club Doha | Indoor Padel in Doha, Qatar</title>',
    '<title>نادي بادل الدوحة | ملاعب بادل مغلقة في الدوحة، قطر</title>')
sub('<meta name="description" content="Five indoor padel courts in Doha. Cooled, lit, and open every day of the year. Book by the court on Playtomic.">',
    '<meta name="description" content="خمسة ملاعب بادل مغلقة في الدوحة. مكيّفة ومضاءة ومفتوحة كل أيام السنة. احجز الملعب عبر Playtomic.">')
# The hreflang set is identical on both pages by spec, so it passes through.
sub('<meta property="og:site_name" content="Padel Club Doha">',
    '<meta property="og:site_name" content="نادي بادل الدوحة">')
sub('<meta property="og:title" content="Padel Club Doha">',
    '<meta property="og:title" content="نادي بادل الدوحة">')
sub('<meta property="og:description" content="Five indoor padel courts in Doha. Cooled, lit, and open every day of the year.">',
    '<meta property="og:description" content="خمسة ملاعب بادل مغلقة في الدوحة. مكيّفة ومضاءة ومفتوحة كل أيام السنة.">')
sub('<meta property="og:locale" content="en">\n<meta property="og:locale:alternate" content="ar">',
    '<meta property="og:locale" content="ar">\n<meta property="og:locale:alternate" content="en">')
sub('<meta property="og:url" content="https://abdallahdarwazeh.github.io/TheDome/">',
    '<meta property="og:url" content="https://abdallahdarwazeh.github.io/TheDome/ar/">')
sub('<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@112,700&family=IBM+Plex+Mono:wght@400&family=IBM+Plex+Sans:wght@400;500&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;700&display=swap" rel="stylesheet">')

# ── type: Arabic wants no tracking, no uppercasing, more leading ──
sub('''  --display:"Archivo",system-ui,sans-serif;
  --body:"IBM Plex Sans",system-ui,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,monospace;''',
    '''  --display:"IBM Plex Sans Arabic",system-ui,sans-serif;
  --body:"IBM Plex Sans Arabic",system-ui,sans-serif;
  --mono:"IBM Plex Sans Arabic",ui-monospace,monospace;''')
sub('h1,h2,h3{font-family:var(--display);font-weight:700;font-stretch:112%;line-height:1.02;letter-spacing:-.02em;margin:0}',
    'h1,h2,h3{font-family:var(--display);font-weight:700;font-stretch:112%;line-height:1.3;margin:0}')
sub('.mono{font-family:var(--mono);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--text-secondary)}',
    '.mono{font-family:var(--mono);font-size:.78rem;color:var(--text-secondary)}')
sub('  display:inline-block;font-family:var(--mono);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;',
    '  display:inline-block;font-family:var(--mono);font-size:.82rem;')
sub('  font-size:clamp(1.55rem,3.5vw,3.5rem);line-height:1.06;letter-spacing:-.022em;',
    '  font-size:clamp(1.5rem,3.3vw,3.3rem);line-height:1.32;')
sub('.event .when{font-family:var(--mono);font-size:.74rem;letter-spacing:.08em;color:var(--accent)}',
    '.event .when{font-family:var(--mono);font-size:.8rem;color:var(--accent)}')
sub('.months{display:flex;justify-content:space-between;font-family:var(--mono);font-size:.66rem;letter-spacing:.06em;color:var(--text-secondary);margin-block-end:.7em}',
    '.months{display:flex;justify-content:space-between;font-family:var(--mono);font-size:.72rem;color:var(--text-secondary);margin-block-end:.7em}')
sub('.dial-table th{font-family:var(--mono);font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--text-secondary);font-weight:400}',
    '.dial-table th{font-family:var(--mono);font-size:.76rem;color:var(--text-secondary);font-weight:400}')

# ── the two rules that are not direction-neutral ──────────────────
sub('  cursor:pointer;list-style:none;padding:1.25em 2.5em 1.25em 0;position:relative;',
    '  cursor:pointer;list-style:none;padding-block:1.25em;padding-inline:0 2.5em;position:relative;')
# mirrored borders put the chevron corner on the other diagonal
sub('  rotate:45deg;transition:rotate .3s ease;',
    '  rotate:-45deg;transition:rotate .3s ease;')
sub('details[open] summary::after{rotate:225deg}',
    'details[open] summary::after{rotate:135deg}')

# ── events block ──────────────────────────────────────────────────
sub('''     Leave the array empty ( [] ) and the whole Events section and
     its nav link remove themselves from the page automatically.''',
    '''     Leave the array empty ( [] ) and the whole Events section and
     its nav link remove themselves from the page automatically.

     This is the Arabic page. Add the event to ../index.html as well,
     with the English wording, or it shows on one language only.''')

# ── chrome ────────────────────────────────────────────────────────
sub('<a class="skip" href="#about">Skip to content</a>',
    '<a class="skip" href="#about">تخطَّ إلى المحتوى</a>')
sub('<a class="brand" href="#top">PADEL CLUB D<span>O</span>HA</a>',
    '<a class="brand" href="#top" dir="ltr">PADEL CLUB D<span>O</span>HA</a>')
sub('aria-controls="nav-list" aria-expanded="false" aria-label="Menu">',
    'aria-controls="nav-list" aria-expanded="false" aria-label="القائمة">')
sub('<nav aria-label="Primary">', '<nav aria-label="التنقل الرئيسي">')
sub('''      <li><a href="#about">The club</a></li>
      <li><a href="#courts">Courts</a></li>
      <li><a href="#academy">Academy</a></li>
      <li id="nav-events" hidden><a href="#events">What is on</a></li>
      <li><a href="#faq">Questions</a></li>
      <li><a href="#contact">Contact</a></li>''',
    '''      <li><a href="#about">النادي</a></li>
      <li><a href="#courts">الملاعب</a></li>
      <li><a href="#academy">الأكاديمية</a></li>
      <li id="nav-events" hidden><a href="#events">الفعاليات</a></li>
      <li><a href="#faq">أسئلة</a></li>
      <li><a href="#contact">تواصل</a></li>''')
sub('<a class="lang" href="/TheDome/ar/" lang="ar" hreflang="ar">العربية</a>',
    '<a class="lang" href="/TheDome/" lang="en" hreflang="en" dir="ltr">English</a>')
# The bar CTA is split so the phone layout can drop the second half.
sub('<a class="cta" href="#book">Book<span class="cta-long"> a court</span></a>',
    '<a class="cta" href="#book">احجز<span class="cta-long"> ملعبًا</span></a>')
sub('<a class="cta" href="#book">Book a court</a>',
    '<a class="cta" href="#book">احجز ملعبًا</a>')      # the static hero

# ── hero: assets sit one level up from /ar/ ───────────────────────
# two stills now: the portrait cut under the device gates, the landscape one
# behind reduced motion on a wide screen
sub('srcset="assets/hero-static-tall.jpg"', 'srcset="../assets/hero-static-tall.jpg"')
sub('srcset="assets/hero-static.jpg"', 'srcset="../assets/hero-static.jpg"')
sub('src="assets/poster.jpg"', 'src="../assets/poster.jpg"')
# both cuts of the hero, now named in JS constants rather than at the fetch
sub('''  var SRC_WIDE = "assets/hero.mp4",
      SRC_TALL = "assets/hero-mobile-tall.mp4",''',
    '''  var SRC_WIDE = "../assets/hero.mp4",
      SRC_TALL = "../assets/hero-mobile-tall.mp4",''')

sub('''        <span class="mono">Outside</span>
        <p>In July, Doha reaches 42 degrees.</p>''',
    '''        <span class="mono">في الخارج</span>
        <p>في يوليو، تبلغ حرارة الدوحة 42 درجة.</p>''')
sub('''        <span class="mono">The law</span>
        <p>From June, the law sends outdoor work home at ten in the morning.</p>''',
    '''        <span class="mono">القانون</span>
        <p>منذ يونيو، يوقف القانون العمل في الهواء الطلق عند العاشرة صباحًا.</p>''')
sub('<p>So the court went under a roof.</p>',
    '<p>فانتقل الملعب إلى تحت سقف.</p>')
sub('''        <span class="mono">Padel Club Doha</span>
        <p>Five courts. Cooled and lit, every day of the year.</p>''',
    '''        <span class="mono">نادي بادل الدوحة</span>
        <p>خمسة ملاعب. مكيّفة ومضاءة، كل أيام السنة.</p>''')

sub('''      <h1>Five courts. One climate you choose.</h1>
      <p>Indoor padel in Doha. Cooled, lit, and open every day of the year.</p>''',
    '''      <h1>خمسة ملاعب. مناخ واحد تختاره.</h1>
      <p>بادل في الدوحة. مكيّف ومضاء ومفتوح كل أيام السنة.</p>''')

# ── 01 the club ───────────────────────────────────────────────────
sub('<span class="mono eyebrow">01 / The club</span>',
    '<span class="mono eyebrow">01 / النادي</span>')
sub('<h2>The building is the argument.</h2>',
    '<h2>المبنى هو الحجة.</h2>')
sub('<p class="lede">The club sits in Doha. Five courts, one roof, and air that stays the same temperature in August as it does in January. Nothing about playing here depends on the weather.</p>',
    '<p class="lede">يقع النادي في الدوحة. خمسة ملاعب تحت سقف واحد، وهواء تبقى حرارته في أغسطس كما هي في يناير. لا شيء في اللعب هنا معلّق على الطقس.</p>')

# ── 02 the courts ─────────────────────────────────────────────────
sub('<span class="mono eyebrow reveal">02 / The courts</span>',
    '<span class="mono eyebrow reveal">02 / الملاعب</span>')
sub('<h2 class="reveal">Glass on four sides, so every ball stays in play.</h2>',
    '<h2 class="reveal">زجاج من الجهات الأربع، فتبقى كل كرة في اللعب.</h2>')
sub('<span>Courts, fully enclosed</span>', '<span>ملاعب مغلقة بالكامل</span>')
sub('<span>Inside, every month of the year</span>', '<span>في الداخل، كل شهر من السنة</span>')
sub('<span>Players to a court, one price between you</span>', '<span>لاعبون في الملعب، وسعر واحد بينكم</span>')
sub('<span>Session to become playable</span>', '<span>حصة واحدة تكفي لتبدأ اللعب</span>')

# ── 03 the reason ─────────────────────────────────────────────────
sub('<span class="mono eyebrow reveal">03 / The reason</span>',
    '<span class="mono eyebrow reveal">03 / السبب</span>')
sub('<h2 class="reveal">Drag through the year. One of these numbers moves.</h2>',
    '<h2 class="reveal">اسحب عبر السنة. رقم واحد فقط يتحرك.</h2>')
sub('          <span class="mono">Outside</span>', '          <span class="mono">في الخارج</span>')
sub('<span class="mono">Inside Padel Club Doha</span>', '<span class="mono">داخل نادي بادل الدوحة</span>')
sub('<label class="sr" for="month">Month of the year</label>',
    '<label class="sr" for="month">شهر السنة</label>')
sub('<p class="dial-caption">Average daily high in Doha, against the temperature held inside the building.</p>',
    '<p class="dial-caption">متوسط درجة الحرارة العظمى في الدوحة، مقابل الحرارة الثابتة داخل المبنى.</p>')
sub('<caption class="sr">Average daily high in Doha compared with the temperature inside Padel Club Doha</caption>',
    '<caption class="sr">متوسط درجة الحرارة العظمى في الدوحة مقارنة بالحرارة داخل نادي بادل الدوحة</caption>')
sub('<thead><tr><th scope="col">Month</th><th scope="col">Outside</th><th scope="col">Inside</th></tr></thead>',
    '<thead><tr><th scope="col">الشهر</th><th scope="col">في الخارج</th><th scope="col">في الداخل</th></tr></thead>')
sub('      NAMES = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],',
    '      NAMES = ["يناير","فبراير","مارس","أبريل","مايو","يونيو","يوليو","أغسطس","سبتمبر","أكتوبر","نوفمبر","ديسمبر"],')
# Arabic has no single-letter month convention, and the initials collide:
# أ alone would stand for April, August and October. Numbers are unambiguous.
sub('      TICKS = ["J","F","M","A","M","J","J","A","S","O","N","D"],',
    '      TICKS = ["1","2","3","4","5","6","7","8","9","10","11","12"],')

# ── 04 the academy ────────────────────────────────────────────────
sub('<span class="mono eyebrow reveal">04 / The academy</span>',
    '<span class="mono eyebrow reveal">04 / الأكاديمية</span>')
sub('<h2 class="reveal">Coaching, in present tense.</h2>',
    '<h2 class="reveal">تدريب، بصيغة الحاضر.</h2>')
sub('<p class="lede reveal">Private and group lessons, for adults and for juniors. Two coaches run the academy.</p>',
    '<p class="lede reveal">دروس خاصة وجماعية، للكبار والناشئين. مدربان يديران الأكاديمية.</p>')
sub('<span class="mono">Coach</span>', '<span class="mono">مدرب</span>', 2)
sub('<h3>Coach A</h3>', '<h3>المدرب أ</h3>')
sub('<h3>Coach B</h3>', '<h3>المدرب ب</h3>')

# ── 05 events ─────────────────────────────────────────────────────
sub('<span class="mono eyebrow reveal">05 / What is on</span>',
    '<span class="mono eyebrow reveal">05 / الفعاليات</span>')
sub('<h2 class="reveal">Coming up at the club.</h2>',
    '<h2 class="reveal">القادم في النادي.</h2>')

# ── 06 questions ──────────────────────────────────────────────────
sub('<span class="mono eyebrow reveal">06 / Questions</span>',
    '<span class="mono eyebrow reveal">06 / أسئلة</span>')
sub('<h2 class="reveal">The things people ask at the desk.</h2>',
    '<h2 class="reveal">ما يسأل عنه الناس عند الاستقبال.</h2>')
sub('<details><summary>Do I need to bring a racket?</summary><p>Rackets and balls are available at the club. Bring court shoes.</p></details>',
    '<details><summary>هل عليّ إحضار مضرب؟</summary><p>المضارب والكرات متوفرة في النادي. أحضر حذاءً مناسبًا للملعب.</p></details>')
sub('<details><summary>Do I need a partner?</summary><p>Padel is played four to a court. If you are short of players, ask at the desk or post in the club group before you book.</p></details>',
    '<details><summary>هل أحتاج إلى شريك؟</summary><p>تُلعب البادل بأربعة لاعبين في الملعب. إن نقص العدد، اسأل عند الاستقبال أو اكتب في مجموعة النادي قبل الحجز.</p></details>')
sub('<details><summary>How do I book?</summary><p>Courts are booked through Playtomic and paid by the court, not per person.</p></details>',
    '<details><summary>كيف أحجز؟</summary><p>تُحجز الملاعب عبر Playtomic، والدفع على الملعب لا على كل لاعب.</p></details>')
sub('<details><summary>Is it actually cooled?</summary><p>Yes. The building is fully enclosed and climate controlled, so the court holds around 24 degrees in August.</p></details>',
    '<details><summary>هل المكان مكيّف فعلًا؟</summary><p>نعم. المبنى مغلق بالكامل ومكيّف، فتبقى حرارة الملعب نحو 24 درجة في أغسطس.</p></details>')
sub('<details><summary>I have never played before. Is that a problem?</summary><p>No experience needed. Padel takes about one session to become playable, which is most of the reason it spread this fast.</p></details>',
    '<details><summary>لم ألعب من قبل. هل هذه مشكلة؟</summary><p>لا حاجة إلى خبرة سابقة. تكفي حصة واحدة تقريبًا لتصبح قادرًا على اللعب، وهذا أكثر ما يفسّر انتشارها بهذه السرعة.</p></details>')
sub('<details><summary>Where is it?</summary><p>In Doha. Parking is on site.</p></details>',
    '<details><summary>أين يقع النادي؟</summary><p>في الدوحة. المواقف متوفرة في الموقع.</p></details>')

# ── 07 contact ────────────────────────────────────────────────────
sub('<span class="mono eyebrow reveal">07 / Contact</span>',
    '<span class="mono eyebrow reveal">07 / تواصل</span>')
sub('<h2 class="reveal">Come and find us.</h2>', '<h2 class="reveal">تعرّف على طريق الوصول.</h2>')
sub('<span class="mono">Where</span><b>Doha</b>',
    '<span class="mono">أين</span><b>الدوحة</b>')
sub('<span class="mono">Instagram</span><b>@padelclubdoha</b>',
    '<span class="mono">إنستغرام</span><b dir="ltr">@padelclubdoha</b>')
sub('<span class="mono">Booking</span><b>Playtomic</b>',
    '<span class="mono">الحجز</span><b dir="ltr">Playtomic</b>')
# Times stay in Latin numerals inside dir=ltr spans; the words around them translate.
sub('<span class="mono">Hours</span><b>6:30 AM – 12:00 AM, daily</b>',
    '<span class="mono">ساعات العمل</span><b><span dir="ltr">6:30</span> صباحًا – <span dir="ltr">12:00</span> منتصف الليل، يوميًا</b>')

# ── 08 book ───────────────────────────────────────────────────────
sub('<span class="mono eyebrow reveal">08 / Book</span>',
    '<span class="mono eyebrow reveal">08 / الحجز</span>')
sub('<h2 class="reveal">It is 42 degrees outside. Play anyway.</h2>',
    '<h2 class="reveal">الحرارة في الخارج 42 درجة. العب رغم ذلك.</h2>')
sub('<a class="cta reveal" href="#" target="_blank" rel="noopener">Book on Playtomic</a>',
    '<a class="cta reveal" href="#" target="_blank" rel="noopener">احجز عبر Playtomic</a>')

# ── footer ────────────────────────────────────────────────────────
sub('''      <span class="mono">Padel Club Doha</span>
      <p>Doha, Qatar</p>''',
    '''      <span class="mono">نادي بادل الدوحة</span>
      <p>الدوحة، قطر</p>''')
sub('''      <span class="mono">Hours</span>
      <p>6:30 AM – 12:00 AM<br>Every day</p>''',
    '''      <span class="mono">ساعات العمل</span>
      <p><span dir="ltr">6:30</span> صباحًا – <span dir="ltr">12:00</span> منتصف الليل<br>كل يوم</p>''')
sub('''      <span class="mono">Language</span>
      <p><a href="/TheDome/" hreflang="en">English</a><br><a href="/TheDome/ar/" lang="ar" hreflang="ar" dir="rtl">العربية</a></p>''',
    '''      <span class="mono">اللغة</span>
      <p><a href="/TheDome/" lang="en" hreflang="en" dir="ltr">English</a><br><a href="/TheDome/ar/" hreflang="ar">العربية</a></p>''')
sub('''      <span class="mono">Follow</span>
      <p><a href="#" target="_blank" rel="noopener">Instagram</a></p>''',
    '''      <span class="mono">تابعنا</span>
      <p><a href="#" target="_blank" rel="noopener">إنستغرام</a></p>''')
sub('<p style="opacity:.55;font-size:.78rem;margin-top:1.5rem">Concept redesign by Upscale Qatar &mdash; not affiliated with Padel Club Doha. <span lang="ar">&#1578;&#1589;&#1605;&#1610;&#1605; &#1605;&#1602;&#1578;&#1585;&#1581;&#1548; &#1594;&#1610;&#1585; &#1578;&#1575;&#1576;&#1593; &#1604;&#1604;&#1606;&#1575;&#1583;&#1610;.</span></p>',
    '<p style="opacity:.55;font-size:.78rem;margin-top:1.5rem">تصميم مقترح من Upscale Qatar &mdash; غير تابع لنادي بادل الدوحة. <span lang="en" dir="ltr">Concept redesign, not affiliated with the club.</span></p>')


html = SRC.read_text(encoding="utf-8")
for old, new, n in R:
    hits = html.count(old)
    if hits != n:
        raise SystemExit(f"expected {n} hit(s), found {hits} for:\n  {old[:110]!r}")
    html = html.replace(old, new)

# the display face carries no width axis in Arabic
html = html.replace("font-stretch:112%;", "")

DST.parent.mkdir(parents=True, exist_ok=True)
DST.write_text(html, encoding="utf-8")

# Tracking breaks Arabic cursive joining, so every letter-spacing rule left
# on the page has to belong to an element that renders Latin text. Two do:
# the PADEL CLUB DOHA wordmark and the toggle back to English, both dir="ltr".
LATIN_OK = 2
spacing = html.count("letter-spacing")
if spacing != LATIN_OK:
    raise SystemExit(f"{spacing} letter-spacing rules survive, expected {LATIN_OK} "
                     f"(the dir=ltr wordmark and language toggle)")
for el in ('<a class="brand" href="#top" dir="ltr">',
           '<a class="lang" href="/TheDome/" lang="en" hreflang="en" dir="ltr">'):
    if el not in html:
        raise SystemExit(f"the element that justifies a letter-spacing rule is gone: {el}")

leftover = [w for w in ("Archivo", "IBM+Plex+Mono", "font-stretch") if w in html]
if leftover:
    raise SystemExit(f"LTR-only tokens survive on the Arabic page: {leftover}")
print(f"wrote {DST} ({len(html.encode()):,} bytes), {len(R)} swaps all matched")
print(f"letter-spacing rules: {spacing}, both on dir=ltr Latin text")
