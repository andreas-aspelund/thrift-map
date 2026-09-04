import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import './ShopMap.css'

// Fix Leaflet's broken default icon paths when bundled with Vite/webpack
import markerIcon2x from 'leaflet/dist/images/marker-icon-2x.png'
import markerIcon from 'leaflet/dist/images/marker-icon.png'
import markerShadow from 'leaflet/dist/images/marker-shadow.png'

delete L.Icon.Default.prototype._getIconUrl
L.Icon.Default.mergeOptions({
  iconUrl: markerIcon,
  iconRetinaUrl: markerIcon2x,
  shadowUrl: markerShadow,
})

// Oslo city centre
const OSLO_CENTER = [59.9139, 10.7522]
const DEFAULT_ZOOM = 13

export default function ShopMap({ shops }) {
  return (
    <MapContainer
      center={OSLO_CENTER}
      zoom={DEFAULT_ZOOM}
      className="leaflet-map"
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {shops.map((shop) => (
        <Marker key={shop.id} position={[shop.lat, shop.lng]}>
          <Popup>
            <div className="popup">
              <strong className="popup-name">{shop.name}</strong>
              {shop.neighborhood && (
                <span className="popup-neighborhood">{shop.neighborhood}</span>
              )}
              <p className="popup-address">{shop.address}</p>
              {shop.notes && <p className="popup-notes">{shop.notes}</p>}
              <a
                className="popup-directions"
                href={`https://www.google.com/maps/dir/?api=1&destination=${shop.lat},${shop.lng}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                Get directions →
              </a>
            </div>
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  )
}
