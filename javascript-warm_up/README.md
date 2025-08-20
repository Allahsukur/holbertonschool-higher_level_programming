🔹 Ümumi məlumatlar
1. Niyə JavaScript möhtəşəmdir?

Çünki web səhifələrin beynidir → HTML quruluşdur, CSS görünüşdür, JS isə məntiqi hərəkətlərdir.

Serverdə də işləyə bilir (Node.js).

Sadə öyrənilir, amma çox güclüdür.

2. JavaScript skriptini necə işlətmək olar?

Faylın əvvəlinə bu sətri yazırsan:

#!/usr/bin/node


Sonra faylı executable edirsən:

chmod +x file.js
./file.js

3. Dəyişənlər və sabitlər necə yaradılır?

let → dəyişən (dəyəri dəyişilə bilər).

const → sabit (dəyişməz).

var → köhnə üsuldur, scope problemi var (artıq tövsiyə edilmir).

4. var, let, const fərqləri

var → function-scope, eyni adda bir neçə dəfə elan edilə bilər.

let → block-scope, eyni adda yenidən elan edilə bilməz.

const → block-scope, dəyişdirilə bilməz (amma obyektlərin içini dəyişmək olar).

5. Məlumat tipləri (Data types)

Primitive:

string → "Hello"

number → 123

boolean → true/false

null

undefined

symbol

bigint

Non-primitive:

object → {key: "value"}

array → [1, 2, 3]

function

6. Şərtlər (if, if...else)
let x = 10;
if (x > 5) {
  console.log("Böyükdür");
} else {
  console.log("Kiçikdir");
}

7. Şərhlər (Comments)

Bir sətir:

// Bu bir şərhdir


Çox sətir:

/* Bu
   çoxsətirli
   şərhdir */

8. Dəyərləri dəyişənlərə vermək
let name = "Şükür";
const age = 22;

9. Döngülər (while və for)
// while
let i = 0;
while (i < 3) {
  console.log(i);
  i++;
}

// for
for (let j = 0; j < 3; j++) {
  console.log(j);
}

10. break və continue
for (let i = 0; i < 5; i++) {
  if (i === 2) continue; // 2-ni atlayır
  if (i === 4) break;    // dayandırır
  console.log(i);
}

11. Funksiya
function salam(ad) {
  return "Salam " + ad;
}
console.log(salam("Şükür"));


Əgər return yazmasan → funksiya undefined qaytarır.

12. Scope (dairə)

Global scope → hər yerdə əlçatandır.

Function scope → ancaq həmin funksiyanın içində işləyir.

Block scope (let, const) → yalnız {} içində işləyir.

13. Riyazi operatorlar

+ toplama

- çıxma

* vurma

/ bölmə

% qalıq

** qüvvət (məs: 2 ** 3 = 8)

14. Dictionary (Obyektlər)
let user = {name: "Şükür", age: 22};
console.log(user.name); // çıxış: Şükür
user.city = "Bakı"; // yeni açar əlavə et

15. Fayl import etmək
// faylda (math.js)
exports.add = (a, b) => a + b;

// başqa faylda
const math = require('./math');
console.log(math.add(2, 3));

⚙️ Tələblər

Faylın əvvəli → #!/usr/bin/node

Ubuntu 20.04 + Node.js 14.x

Kod üslubu → semistandard (AirBnB style + ; )

Hər faylın sonunda newline olmalıdır

Faylları chmod +x file.js ilə icra edilə bilən hala gətirməlisən