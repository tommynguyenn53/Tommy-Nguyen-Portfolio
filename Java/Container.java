public class Container<T> {
    private T element;

    public Container(T element) {
        this.element = element;
    }

    public boolean isNull() {
        return element == null;
    }

    public void setElement(T element) {
        this.element = element;
    }

    public T getElement() {
        return element;
    }
}
