#!/usr/local/bin/perl
# enter.cgi
#
# �b�f�h�Ńp�X���[�h���� v1.0 is Free. (c)rescue.ne.jp 
#
# |-bin
# |-dev
# |-etc
# |-<b>private_html</b>�i�V�K�ɍ쐬����j�T�[�o�ɂ���Ă͐V�K�쐬�������Ȃ��ꍇ������܂�
# |       |
# |       |-- 401.html�i�F�؂���Ȃ������ꍇ�ɕ\������j
# |       |-- 404.html�i�F�؂��ꂽ���t�@�C�����Ȃ��ꍇ�ɕ\������j
# |       |-- �����ɔF�،�ɕ\��������t�@�C����u��
# |       |-- �����ł��ݒu�ł���
# |       |-- �����ɒu�����t�@�C�����̓p�X���[�h���͉�ʂg�s�l�k��<option>�Ŏw�肷��
# |
# |-public_html
# |       |
# |       |--private�i�C�ӂ̃f�B���N�g���j
# |             |-- enter.cgi�i���̃X�N���v�g�j
# |             |-- index.html�i�p�X���[�h���̓t�H�[���j
# |-usr
#

# enter.cgi���猩��private_html�f�B���N�g���̈ʒu�w��
# ��L�̍\���Ȃ�΂��̂܂܂ł悢
$private_html = './';

# ID�Ƃ���ɑΉ������p�X���[�h��ݒ肷��i�����ւ��Ă��������j
# ���Ȃ炸0����̈�A�ԍ���t���邱�Ɓi�����ł����₹�܂��j
# ����enter.cgi�𑼂̃��[�U���猩���Ă��܂��悤�ȃT�[�o�ł́A
# ����enter.cgi�̃p�[�~�b�V������705�ɂ���Ȃǂ��đΉ����Ă��������B
# ���b�V���ł�755�łn�j�ł��B
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

   # ��L sub html ��404.html���������Ƃ��ł��܂����A������404.html���J���Ȃ��ꍇ�A
   # �������[�v���N�����Ă��܂��̂ŁA���̃��[�`����ʂɕt���܂����B���̃��[�`���ɂ�
   # �G���[���������Ă��܂���̂ŁA404.html���J���Ȃ��ꍇ�̓T�[�o�G���[�ɂȂ�܂��B

   open(HTML,"$private_html\/404.html");
   @lines = <HTML>;
   close(HTML);

   print 'Content-type: text/html' ."\n\n";
   foreach (@lines) { print; }
   exit;
}
