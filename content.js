var elements = document.getElementsByTagName('span');

var quiet_mush = {
    'с': ['ϲ', 'င'],
    'е': ['e', 'e'],
    'ш': ['Ⱎ'],
    'ё': ['ë'],
    'т': ['ፐ'],
    'и': ['ͷ'],
    'х': ['χ'],
    'м': ['ӎ', 'μ'],
    'я': ['ѣ'],
    'г': ['γ', 'r'],
    'к': ['κ','ϰ','κ'],
    'ф': ['Ⱇ', 'ϕ', 'φ'],
    'р': ['ρ'],
    'а': ['a', 'α', 'ɑ'],
    'у': ['y', 'ყ'],
    'з': ['з'],
    'б': ['ϭ'],
    'л': ['ʌ'],
    'о': ['ဝ', 'ဝ'],
    'в': ['ʙ'],
    'ы': ['ꙑ'],
    'п': ['π'],
    'ч': ['ɥ'],
    'С': ['C', 'Ϲ', 'Ⅽ'],
    'Ъ': ['Ҍ'],
    'Е': ['Ε'],
    'Ш': ['Ɯ'],
    'Т': ['Τ', 'T'],
    'И': ['Ͷ'],
    'Х': ['Χ'],
    'М': ['Μ'],
    'Г': ['Γ'],
    'К': ['Κ', 'Κ'],
    'Ф': ['Φ'],
    'Р': ['Ρ'],
    'А': ['Α', 'A'],
    'Н': ['ᚺ'],
    'У': ['Y'],
    'З': ['Ვ'],
    'Б': ['Ϭ'],
    'Л': ['Λ'],
    'О': ['O', 'ഠ', 'ഠ'],
    'В': ['B'],
    'Ы': ['Ꙑ'],
    'П': ['Π'],
    'Й': [''],
    'Ч': ['Ɥ'],
    'a': ['a', 'ɑ'],
    'q': ['ԛ'],
    'u': ['Ս', 'ս'],
    'i': ['ɪ'],
    'c': ['с', 'ϲ', 'င'],
    'k': ['κ','κ'],
    'r': ['г'],
    'o': ['o', 'ဝ', 'ဝ'],
    'w': ['ԝ'],
    'n': ['ո', ],
    'f': ['ϝ'],
    'x': ['χ'],
    'j': ['յ'],
    'm': ['ᛖ'],
    'p': ['ρ'],
    's':  ['ѕ', 'Տ', 'Ჽ'],
    'v': ['∨', '⋎'],
    'h': ['հ'],
    'l': ['ι'],
    'z': ['ⴭ'],
    'y': ['ყ'],
    'd': ['ԁ'],
    'g': ['ց', 'g'],
    'A': ['Α'],
    'Q': ['Ǫ'],
    'U': ['Ս'],
    'I': ['Ɪ'],
    'C': ['С', 'Ϲ', 'Ⅽ'],
    'K': ['Κ', 'Κ'],
    'B': ['Β'],
    'O': ['ഠ', 'Ჿ'],
    'W': ['Ԝ'],
    'N': ['Ν'],
    'F': ['Ϝ'],
    'X': ['Χ'],
    'J': ['Ј', 'Ϳ'],
    'M': ['Ϻ'],
    'P': ['Р', 'Ρ'],
    'S': ['Ѕ', 'Ꚃ', 'ട', 'ჽ'],
    'V': ['Ⅴ'],
    'E': ['Ε'],
    'T': ['Τ'],
    'H': ['Η', 'Н'],
    'L': ['Ⅼ', 'Լ'],
    'Z': ['Ζ'],
    'Y': ['У'],
    'D': ['Ⅾ'],
    'G': ['Ԍ'],
}

var pretty_mush = {
    ' ': ['·'],
    'с': ['c', 'ć', 'ϲ', 'င'],
    'ъ': ['ҍ'],
    'е': ['є', 'ϵ', 'é'],
    'ш': ['š', 'Ⱎ', 'w', 'ɯ'],
    'ь': ['♭'],
    'щ': ['ѱ'],
    'ё': ['ø'],
    'э': ['ѥ', 'æ'],
    'т': ['τ'],
    'и': ['i'],
    'х': ['χ'],
    'м': ['ӎ', 'μ'],
    'я': ['ѣ'],
    'г': ['γ', 'r'],
    'к': ['κ','ϰ','κ'],
    'ф': ['Ⱇ', 'ϕ', 'φ'],
    'р': ['ρ'],
    'а': ['a', 'α', 'ɑ'],
    'н': ['ᚻ'],
    'у': ['y', 'ყ'],
    'з': ['з', 'ꙁ', 'ȝ'],
    'б': ['ҕ', 'ϭ'],
    'л': ['λ', '人'],
    'о': ['ဝ', 'ဝ'],
    'в': ['ʙ'],
    'ы': ['ꙑ'],
    'п': ['π', 'ㄇ'],
    'й': ['ї'],
    'ч': ['ɥ', 'ⴗ', 'ϥ'],
    'С': ['C', 'Ϲ', 'Ⅽ'],
    'Ъ': ['Ҍ'],
    'Е': ['Є', 'Ε'],
    'Ш': ['Š', 'W', 'Ɯ'],
    'Ь': ['♭'],
    'Щ': ['Ѱ'],
    'Ё': ['Ø'],
    'Э': ['Ѥ', 'Æ'],
    'Т': ['Τ'],
    'И': ['I'],
    'Х': ['Χ'],
    'М': ['Ӎ', 'Μ'],
    'Я': ['Ѣ'],
    'Г': ['Γ'],
    'К': ['Κ', 'Κ'],
    'Ф': ['Φ', 'Θ'],
    'Р': ['Ρ'],
    'А': ['Α', 'A', 'Ɑ'],
    'Н': ['Ν', 'ᚺ', 'ਮ'],
    'У': ['Ყ', 'Y'],
    'З': ['Յ', 'Პ', 'Ȝ'],
    'Б': ['Ҕ', 'Ϭ'],
    'Л': ['Λ', '人'],
    'О': ['O', 'Ꙩ', 'Ѻ', 'ഠ', 'ഠ'],
    'В': ['B'],
    'Ы': ['Ꙑ'],
    'П': ['Π', '冂'],
    'Й': ['Ї'],
    'Ч': ['Ɥ',  'Ⴗ', 'ㄐ'],
    'a': ['a', 'α', 'ɑ'],
    'q': ['ԛ', 'գ', 'ǫ'],
    'u': ['Ս', 'ս'],
    'i': ['ɪ'],
    'c': ['с', 'ć', 'ϲ', 'င'],
    'k': ['κ','ϰ','κ'],
    'b': ['♭', 'β'],
    'r': ['г', 'ρ'],
    'o': ['o', 'ဝ', 'ဝ'],
    'w': ['ш', 'ԝ'],
    'n': ['ո', 'ⴖ', 'п'],
    'f': ['ϝ', 'ғ', 'բ'],
    'x': ['χ'],
    'j': ['յ', 'ȷ'],
    'm': ['ϻ', 'ᛖ'],
    'p': ['р', 'ρ'],
    's':  ['ѕ','ꚃ', 'Տ', 'Ჽ'],
    'v': ['ѵ', '∨', '⋎'],
    'e': ['є', 'ϵ', 'é'],
    't': ['τ'],
    'h': ['Һ', 'һ', 'հ', 'Ⴙ'],
    'l': ['ι', '|', 'Ӏ'],
    'z': ['Հ', 'ⴭ', 'ℤ'],
    'y': ['у', 'ყ', 'ⴘ'],
    'd': ['Ԁ', 'ԁ', 'Ძ', 'ძ'],
    'g': ['ɡ', 'ց', 'g'],
    'A': ['Α', 'Ɑ'],
    'Q': ['Ǫ', 'Ԛ', 'Ⴍ', 'Ⴓ'],
    'U': ['ሀ', 'Ս'],
    'I': ['Ɪ'],
    'C': ['С', 'Ϲ', 'Ⅽ'],
    'K': ['Κ', 'Κ'],
    'B': ['Β', 'ẞ', 'ß'],
    'R': ['ρ', 'Я'],
    'O': ['ഠ', 'Ჿ'],
    'W': ['Ԝ', 'Ш'],
    'N': ['Ν', 'ᚺ'],
    'F': ['Ϝ', 'Ғ', 'Բ'],
    'X': ['Χ'],
    'J': ['Ј', 'Ϳ'],
    'M': ['Ϻ', 'ℳ', 'ᛖ'],
    'P': ['Р', 'Ρ'],
    'S': ['Ѕ', 'Ꚃ', 'Ⴝ', 'ട', 'ჽ'],
    'V': ['Ѵ', 'Ⅴ', '⋁'],
    'E': ['Є', 'Ε'],
    'T': ['Τ'],
    'H': ['Η', 'Н', 'н', 'ዘ', 'ਮ'],
    'L': ['Ⅼ', 'Լ', 'լ', 'ւ'],
    'Z': ['Ζ', 'Ⴭ', '乙'],
    'Y': ['У', 'Ყ', 'Ⴘ'],
    'D': ['Ⅾ'],
    'G': ['Ԍ', 'ԍ', 'ɢ'],
}

var mush = function (e, threshold) {
    threshold = Number(threshold);
    var mushType;
    chrome.storage.sync.get({
        mushType: 'quiet',
    }, function(items) {
        mushType = items.mushType;
    })
    var mushdata;
    if (mushType == 'quiet') {
        mushdata = quiet_mush;
    } else {
        mushdata = pretty_mush;
    }

    var ret = '';
    for (var i = 0; i < e.length; i++) {
        if (Math.random() < threshold) {
            if (e[i] in mushdata) {
                ret += mushdata[e[i]][Math.floor(Math.random()*mushdata[e[i]].length)]
            } else {
                ret += e[i]
            }
        } else {
            ret += e[i]
        }
    }
    return ret
}

var keyListener = function (e) {
    chrome.storage.sync.get({
        triggerButton: 'F20',
        threshold: 0.4
    }, function(items) {
        var triggerButton = items.triggerButton;
        var threshold = items.threshold;
        if (e.key == triggerButton) {
            elem = document.activeElement;
            elem.innerText = mush(elem.innerText, threshold);
        }
    })

};

addEventListener("keyup", keyListener);