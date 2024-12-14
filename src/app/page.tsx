import { Layout } from "@/components/layout";
import { Music, Images, Search } from "lucide-react";
import Link from "next/link";

export default function HomePage() {
	return (
		<Layout>
			<div className="flex flex-col items-center justify-center min-h-[calc(100vh-4rem)] px-4 py-12">
				<h1 className="ml-5 text-5xl font-extrabold mb-6 flex items-center">
					SongSmart
					<Search className="ml-2" height={50} width={50} />
				</h1>
				<p className="text-xl text-center max-w-2xl mb-12">
					Discover music in new ways. Search songs by audio or album
					artwork with our recognition technology.
				</p>
				<div className="grid grid-cols-1 sm:grid-cols-2 gap-8 w-full max-w-4xl">
					<Link href="/search/audio">
						<div className="bg-[white] border-black rounded-2xl p-6 border-2 hover:border-sky-400 hover:bg-sky-50 active:bg-sky-100 shadow-md hover:shadow-2xl transition transform hover:-translate-y-2 flex flex-col items-center justify-center space-y-4 text-center">
							<Music
								className="text-sky-500 transition-colors duration-300"
								size={64}
								strokeWidth={1.5}
							/>
							<h2 className="text-xl font-semibold transition-colors">
								Search by Audio
							</h2>
							<p className="text-sm">
								Upload WAV/MIDI and find matching songs
							</p>
						</div>
					</Link>

					<Link href="/search/album">
						<div className="bg-white border-black rounded-2xl p-6 border-2 hover:border-emerald-400 hover:bg-emerald-50 active:bg-emerald-100 shadow-md hover:shadow-2xl transition transform hover:-translate-y-2 flex flex-col items-center justify-center space-y-4 text-center">
							<Images
								className="text-emerald-500 transition-colors duration-300"
								size={64}
								strokeWidth={1.5}
							/>
							<h2 className="text-xl font-semibold transition-colors">
								Search by Album
							</h2>
							<p className="text-sm">
								Identify songs from album covers
							</p>
						</div>
					</Link>
				</div>
			</div>
		</Layout>
	);
}
