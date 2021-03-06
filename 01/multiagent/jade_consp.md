Краткий конспект по руководству программиста для JADE
========================

[Краткое руководство программиста на английском языке](http://jade.tilab.com/doc/programmersguide.pdf).

[JADE](http://jade.tilab.com/dl.php?file=JADE-all-4.3.3.zip) (Java Agent Development Framework) -- фрэймворк для разработки мультиагентных систем, написанный на Java.

Для полного понимания JADE рекомендуется изучить следующие документы:

* [Agent Management Specifications (FIPA no. 23)](http://www.fipa.org/specs/fipa00023/SC00023K.pdf)
* [Agent Communication Language]()
* [ACL Message Structure (FIPA no. 61)](http://www.fipa.org/specs/fipa00061/SC00061G.pdf)

Конфигурация IDE
------------------------
Запуск из консоли
``` Bash
$ java jade.Boot -gui AgetnName:examples.hello.HelloWorldAgent
```
### Netbeans
Для того, чтобы можно было запускать приложение из NetBeans:
* Правый клик по проекту в обозревателе проектов -> set configuration -> Customize
* Пункт Run
* В качестве Main class указать jade.Boot
* В качестве Arguments указать -gui

### Eclipse
Инструкиця [тут] (https://wrjih.wordpress.com/2008/11/29/running-jade-under-eclipse/).

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
