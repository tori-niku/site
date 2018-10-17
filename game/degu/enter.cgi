#!/usr/local/bin/perl
# enter.cgi
#
# ＣＧＩでパスワード制限 v1.0 is Free. (c)rescue.ne.jp 
#
# |-bin
# |-dev
# |-etc
# |-<b>private_html</b>（新規に作成する）サーバによっては新規作成権限がない場合があります
# |       |
# |       |-- 401.html（認証されなかった場合に表示する）
# |       |-- 404.html（認証されたがファイルがない場合に表示する）
# |       |-- ここに認証後に表示させるファイルを置く
# |       |-- いくつでも設置できる
# |       |-- ここに置いたファイル名はパスワード入力画面ＨＴＭＬの<option>で指定する
# |
# |-public_html
# |       |
# |       |--private（任意のディレクトリ）
# |             |-- enter.cgi（このスクリプト）
# |             |-- index.html（パスワード入力フォーム）
# |-usr
#

# enter.cgiから見たprivate_htmlディレクトリの位置指定
# 上記の構成ならばこのままでよい
$private_html = './';

# IDとそれに対応したパスワードを設定する（書き替えてください）
# かならず0からの一連番号を付けること（いくつでも増やせます）
# このenter.cgiを他のユーザから見られてしまうようなサーバでは、
# このenter.cgiのパーミッションを705にするなどして対応してください。
# メッシュでは755でＯＫです。
#---------------------------------------------------------------------
$ID[0] = 'test';           $PW[0] = 'say';
$ID[1] = '1st';             $PW[1] = 'SAY';
#---------------------------------------------------------------------

if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); }
else { $buffer = $ENV{'QUERY_STRING'}; }

@pairs = split(/&/,$buffer);
foreach $pair (@pairs)
{
    ($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $FORM{$name} = $value;
}

$members = @ID;
foreach (0 .. $members -1) {

  if ($FORM{'password'} eq $PW[$_]) { $target = $FORM{'target'}; &html; }
}

$target = '401.html'; &html;


sub html {

   if (!open(HTML,"$private_html\/$target")) { &html404; }
   @lines = <HTML>;
   close(HTML);

   print 'Content-type: text/html' ."\n\n";
   foreach (@lines) { print; }
   exit;
}

sub html404 {

   # 上記 sub html で404.htmlを扱うことができますが、万が一404.htmlが開けない場合、
   # 無限ループを起こしてしまうので、このルーチンを別に付けました。このルーチンには
   # エラー処理をしていませんので、404.htmlが開けない場合はサーバエラーになります。

   open(HTML,"$private_html\/404.html");
   @lines = <HTML>;
   close(HTML);

   print 'Content-type: text/html' ."\n\n";
   foreach (@lines) { print; }
   exit;
}
