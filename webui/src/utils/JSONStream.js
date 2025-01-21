export default class JSONStream {
  constructor(options = {}) {
    this.objectMode = options.objectMode || true;
    this.async = options.async || false;
    this.buffer = "";
  }

  transform(data, callback) {
    if (typeof data !== "string") {
      data = data.toString();
    }

    this.buffer += data;

    let start = 0;
    for (let ptr = 0; ptr < this.buffer.length; ptr++) {
      if (this.buffer[ptr] === "}" && (this.buffer[ptr+1] === "{" || ptr === this.buffer.length - 1)) {
        let line = null;
        try {
          line = JSON.parse(this.buffer.slice(start, ptr+1));
        } catch (ex) {
          console.error('Parsing error:', ex);
          continue; // Skip to next cycle if parsing fails
        }

        if (line) {
          if (this.async) {
            setTimeout(() => callback(null, line), 0);
          } else {
            callback(null, line);
          }
          line = null;
        }

        start = ptr + 1;
      }
    }

    this.buffer = this.buffer.slice(start); // Keep unparsed part of the buffer
  }
}
