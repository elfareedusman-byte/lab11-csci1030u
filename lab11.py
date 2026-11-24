# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.
import asyncio
import socket


async def gather_doubled(numbers):
    # Outline:
    # Define a small async helper coroutine that takes a single number and returns n * 2.
    # Create one coroutine per number in numbers, run all of them concurrently with
    # asyncio.gather(*coros), and return the resulting list in the original order.
    async def double(n):
        return n * 2

    return await asyncio.gather(*(double(n) for n in numbers))


async def fastest(jobs):
    # Outline:
    # Define an async worker coroutine that awaits asyncio.sleep(delay) and returns label.
    # Start all job coroutines at once using asyncio.as_completed(coros).
    # Await the very first completed coroutine in the loop, cancel any remaining pending
    # tasks so they don't keep running, and return that winning label.
    async def run_job(label, delay):
        await asyncio.sleep(delay)
        return label

    tasks = [asyncio.create_task(run_job(label, delay)) for label, delay in jobs]
    for finished in asyncio.as_completed(tasks):
        winner = await finished
        for t in tasks:
            if not t.done():
                t.cancel()
        return winner


def echo_once(host, port, message):
    # Outline:
    # Create a TCP socket (AF_INET, SOCK_STREAM) inside a with block so it closes cleanly.
    # Connect to (host, port), encode message to bytes and send all of it,
    # receive up to 1024 bytes back from the server, decode to string, and return it.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        data = s.recv(1024)
        return data.decode()

def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()
