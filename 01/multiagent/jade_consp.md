Краткий конспект по руководству программиста для JADE
========================

[Краткое руководство программиста на английском языке](http://jade.tilab.com/doc/programmersguide.pdf).

JADE (Java Agent Development Framework) -- фрэймворк для разработки мультиагентных систем, написанный на Java.

Для полного понимания JADE рекомендуется изучить следующие документы:
	* [Agent Management Specifications (FIPA no. 23)](http://www.fipa.org/specs/fipa00023/SC00023K.pdf)
	* [Agent Communication Language]()
	* [ACL Message Structure (FIPA no. 61)](http://www.fipa.org/specs/fipa00061/SC00061G.pdf)

Конфигурация IDE
------------------------
Запуск из консоли
``` Bash
$ java jade.Boot -gui AgentName:examples.hello.HelloWorldAgent
```

Для того, чтобы можно было запускать приложение из NetBeans:
	* Правый клик по проекту в обозревателе проектов -> set configuration -> Customize
	* Пункт Run
	* В качестве Main class указать jade.Boot
	* В качестве Arguments указать -gui

Hello, World!
---------------------

``` Java
import jade.core.Agent;

public class hello_world extends Agent {
	protected void setup() {
		System.out.println("Hello World!");
	}
}
```
