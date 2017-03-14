from nose.tools import *
from NAME.sentenc import *
from NAME import lexicon

object_verb=lexicon.scan("bear eat princess")
verb=lexicon.scan("go north")
verb1=lexicon.scan("go north")
verb_stop=lexicon.scan("go to the north")
stop_start1=lexicon.scan("the of north of")
stop_start=lexicon.scan("the of north of")

def test_sentence():
	sentence=Sentence(("subject","bear"),("verb","eat"),("object","princess"))
	assert_equal(sentence.subject,"bear")
	assert_equal(sentence.verb,"eat")
	assert_equal(sentence.object,"princess")

def test_peek():
	peek_o_v=peek(object_verb)
	peek_v=peek(verb)
	peek_v_s=peek(verb_stop)
	assert_equal(peek_o_v,"noun")
	assert_equal(peek_v,"verb")
	assert_equal(peek_v_s,"verb")

def test_match():
	match_o_v=match(object_verb,"noun")
	match_v=match(verb,"noun")
	match_none=match(None,"noun")
	assert_equal(match_o_v,("noun","bear"))
	assert_equal(match_v,None)
	assert_equal(match_none,None)

def test_skip():
	skip(stop_start,"stop")
	assert_equal(stop_start,[("direction","north"),("stop","of")])
	
def test_parse_verb():
	parse_verb_v=parse_verb(verb1)
	assert_equal(parse_verb_v,("verb","go"))
	assert_raises(ParserError,parse_verb,stop_start1)




obj_N1=lexicon.scan("go north")
obj_N2=lexicon.scan("to the north")
obj_Y1=lexicon.scan("the of north of")
obj_Y2=lexicon.scan("bear of")
def test_parse_object():
	assert_raises(ParserError,parse_object,obj_N1)
	assert_raises(ParserError,parse_object,obj_N2)
	parse_obj_Y1=parse_object(obj_Y1)
	parse_obj_Y2=parse_object(obj_Y2)
	assert_equal(parse_obj_Y1,("direction","north"))
	assert_equal(parse_obj_Y2,("noun","bear"))




sub1=("noun","bear")
sub2=("noun","player")
sub3=("verb","go")
sub_Y0=lexicon.scan("go north of")
sub_Y1=lexicon.scan("go north of")
sub_Y2=lexicon.scan("the eat the bear of")
sub_N1=lexicon.scan("north go")
def test_parse_subject():
	parse_sub_Y1=parse_subject(sub_Y1,sub1)
	parse_sub_Y2=parse_subject(sub_Y2,sub2)
	parse_sub_Y3=parse_subject(sub_Y0,sub3)
	assert_equal(parse_sub_Y1.subject,"bear")
	assert_equal(parse_sub_Y1.verb,"go")
	assert_equal(parse_sub_Y1.object,"north")
	assert_equal(parse_sub_Y2.subject,"player")
	assert_equal(parse_sub_Y2.verb,"eat")
	assert_equal(parse_sub_Y2.object,"bear")
	assert_equal(parse_sub_Y3.subject,"go")
	assert_equal(parse_sub_Y3.verb,"go")
	assert_equal(parse_sub_Y3.object,"north")
	assert_raises(ParserError,parse_subject,sub_N1,sub3)




sentence_Y1=lexicon.scan("bear eat princess")
sentence_Y2=lexicon.scan("eat princess")
sentence_N1=lexicon.scan("princess")
sentence_N2=lexicon.scan("north eat")
sentence_N3=lexicon.scan("north eat princess")
def test_parse_sentence():
	par_sen_1=parse_sentence(sentence_Y1)
	par_sen_2=parse_sentence(sentence_Y2)
	assert_equal(par_sen_1.subject,"bear")
	assert_equal(par_sen_1.verb,"eat")
	assert_equal(par_sen_1.object,"princess")
	assert_equal(par_sen_2.subject,"player")
	assert_equal(par_sen_2.verb,"eat")
	assert_equal(par_sen_2.object,"princess")
	assert_raises(ParserError,parse_sentence,sentence_N1)
	assert_raises(ParserError,parse_sentence,sentence_N2)
	assert_raises(ParserError,parse_sentence,sentence_N3)
	
	
			
					
					


		
		
