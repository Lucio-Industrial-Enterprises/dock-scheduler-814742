"""Shipping rate calculations."""

_SERVICES = {"standard", "express"}
_EXPRESS_SURCHARGE = 7.0


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone — ``"local"`` or ``"regional"``.
        service: ``"standard"`` (default) or ``"express"``.

    Returns:
        Quoted price in US dollars.

    Raises:
        ValueError: If weight is non-positive, zone is unknown, or service is unknown.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in _SERVICES:
        raise ValueError(f"unknown service: {service!r}")
    base = 5.0 if zone == "local" else 8.0
    quote = base + 1.5 * weight_kg
    if service == "express":
        quote += _EXPRESS_SURCHARGE
    return round(quote, 2)
