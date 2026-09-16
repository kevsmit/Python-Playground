#!/usr/bin/env python3
"""Run a quick set of network troubleshooting checks."""

from __future__ import annotations

import platform
import socket
import subprocess
from dataclasses import dataclass


@dataclass
class CheckResult:
    name: str
    passed: bool
    details: str


def get_computer_info() -> list[CheckResult]:
    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
        ip_result = CheckResult("Local IP", True, local_ip)
    except socket.gaierror as error:
        ip_result = CheckResult("Local IP", False, str(error))

    return [
        CheckResult("Computer name", True, hostname),
        CheckResult("Operating system", True, platform.platform()),
        ip_result,
    ]


def check_dns(domain: str = "example.com") -> CheckResult:
    try:
        addresses = sorted({item[4][0] for item in socket.getaddrinfo(domain, None)})
        return CheckResult("DNS resolution", True, f"{domain} -> {', '.join(addresses)}")
    except socket.gaierror as error:
        return CheckResult("DNS resolution", False, f"{domain}: {error}")


def check_port(host: str, port: int, timeout: float = 3.0) -> CheckResult:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return CheckResult(
                f"TCP connection ({host}:{port})",
                True,
                "Connection successful",
            )
    except OSError as error:
        return CheckResult(
            f"TCP connection ({host}:{port})",
            False,
            str(error),
        )


def check_ping(host: str = "1.1.1.1") -> CheckResult:
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", count_flag, "1", host]

    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=6,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as error:
        return CheckResult(f"Ping ({host})", False, str(error))

    if completed.returncode == 0:
        return CheckResult(f"Ping ({host})", True, "Reply received")

    output = (completed.stderr or completed.stdout).strip()
    return CheckResult(f"Ping ({host})", False, output or "No reply received")


def print_report(results: list[CheckResult]) -> None:
    print("\nNETWORK TROUBLESHOOTING REPORT")
    print("=" * 32)

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"[{status}] {result.name}")
        print(f"       {result.details}")

    passed = sum(result.passed for result in results)
    failed = len(results) - passed

    print("-" * 32)
    print(f"Summary: {passed} passed, {failed} failed")

    if failed == 0:
        print("Your basic network checks look healthy.")
    else:
        print("One or more checks failed. Review the failed item(s) above.")


def main() -> None:
    results = get_computer_info()
    results.extend(
        [
            check_dns(),
            check_port("example.com", 80),
            check_port("example.com", 443),
            check_ping(),
        ]
    )
    print_report(results)


if __name__ == "__main__":
    main()
