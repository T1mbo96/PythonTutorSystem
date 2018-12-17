var editor;

function outf(text) {
    var mypre = document.getElementById("output");
    mypre.innerHTML = mypre.innerHTML + text;
}

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function runit() {
    var prog = editor.getDoc().getValue();
    var mypre = document.getElementById("output");
    mypre.innerHTML = '';
    Sk.pre = "output";
    Sk.configure({output: outf, read: builtinRead});
    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
    var myPromise = Sk.misceval.asyncToPromise(function () {
        return Sk.importMainWithBody("<stdin>", false, prog, true);
    });
    myPromise.then(function (mod) {
            console.log('success');
        },
        function (err) {
            console.log(err.toString());
            outf(err.toString());
        });
    hide_alerts();
}

function run() {
    runit();
    test_code();
}

function hide_alerts() {
    document.getElementById('wrong').style.display = 'none';
    document.getElementById('correct').style.display = 'none';
}

$(document).ready(function () {
    //code here...
    var code = $("#custom_code")[0];
    editor = CodeMirror.fromTextArea(code, {
        lineNumbers: true,
        mode: "python",
    });
});

function test_code() {
    var _output = document.getElementById('output').innerText;
    if(_output==="50\n") {
        show_success_alert();
    } else {
        show_danger_alert();
    }
}

function show_success_alert() {
    if (document.getElementById('correct').style.display === 'none') {
        if (document.getElementById('wrong').style.display === 'block') {
            document.getElementById('wrong').style.display = 'none';
        }
        document.getElementById('correct').style.display = 'block';
    }
}

function show_danger_alert() {
    if (document.getElementById('wrong').style.display === 'none') {
        if (document.getElementById('correct').style.display === 'block') {
            document.getElementById('correct').style.display = 'none';
        }
        document.getElementById('wrong').style.display = 'block';
    }
}