class Deque {
	front: any;
	back: any;
    constructor() {
        this.front = this.back = undefined;
    }

    getLength() {
        let len = 0;
        let current = this.back;
        while (current) {
            current = current.next;
            len++;
        }
        return (len);
    }

    addFront(value: any) {
        if (!this.front) this.front = this.back = { value };
        else this.front = this.front.next = { value, prev: this.front };
    }
    removeFront() {
        const value = this.peekFront();
        if (this.front === this.back) this.front = this.back = undefined;
        else (this.front = this.front.prev).next = undefined;
        return value;
    }
    peekFront() {
        return this.front && this.front.value;
    }
    addBack(value: any) {
        if (!this.front) this.front = this.back = { value };
        else this.back = this.back.prev = { value, next: this.back };
    }
    removeBack() {
        const value = this.peekBack();
        if (this.front === this.back) this.front = this.back = undefined;
        else (this.back = this.back.next).back = undefined;
        return value;
    }
    peekBack() {
        return this.back && this.back.value;
    }
}

export { Deque }
