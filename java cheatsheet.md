# Java snippet

## Stack trace

```java
            StackTraceElement[] stackTraceElements = Thread.currentThread().getStackTrace();
            System.out.println("stack trace");
            for (StackTraceElement stackTraceElement : stackTraceElements) {
                System.out.println(stackTraceElement.toString());
            }
```
